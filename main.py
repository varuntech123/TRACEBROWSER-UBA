from flask import Flask, request, render_template_string, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

activity_logs = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Pehchaan AI – Professional UBA Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        body { margin:0; background:#0b1220; color:#e5e7eb; font-family: Inter, sans-serif; overflow: hidden; }
        .header { padding:15px 25px; display:flex; justify-content:space-between; align-items:center; background:#020617; border-bottom:1px solid #1f2937; }
        .header h1 { font-size:18px; color: #38bdf8; margin:0; font-weight: 700; letter-spacing: 1px; }
        
        .container { display:flex; height: calc(100vh - 60px); }
        
        /* SIDEBAR STYLING */
        .sidebar { width:260px; background:#020617; border-right:1px solid #1f2937; padding:20px; }
        .sidebar h3 { color:#9ca3af; font-size: 12px; text-transform: uppercase; margin-bottom: 20px; letter-spacing: 1px; }
        .filter { 
            background:#111827; padding:12px; margin-bottom:8px; border-radius:8px; 
            cursor:pointer; font-size: 13px; transition: all 0.2s; border: 1px solid transparent;
        }
        .filter:hover { background:#1f2937; border-color: #38bdf8; }
        .filter.active { background:#1e293b; border-left: 4px solid #38bdf8; color: #38bdf8; font-weight: 600; }

        .main { flex:1; padding:25px; overflow-y:auto; background: #0f172a; }
        
        /* STAT CARDS */
        .cards { display:grid; grid-template-columns: repeat(4, 1fr); gap:15px; margin-bottom:25px; }
        .card { background:#020617; padding:20px; border-radius:12px; border:1px solid #1f2937; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
        .card h2 { margin:0; font-size:28px; color:#38bdf8; }
        .card span { color:#9ca3af; font-size:12px; font-weight: 500; }

        /* TABLE STYLING */
        .table-container { background: #020617; border-radius: 12px; border: 1px solid #1f2937; overflow: hidden; }
        table { width:100%; border-collapse:collapse; }
        th { background:#111827; text-align:left; padding:15px; font-size:11px; color:#9ca3af; text-transform: uppercase; letter-spacing: 1px; }
        td { padding:14px; border-top:1px solid #1f2937; font-size:13px; vertical-align: middle; }
        tr:hover { background: #0f172a; }
        
        .url-link { color: #64748b; font-size: 11px; text-decoration: none; display: block; max-width: 400px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
        .url-link:hover { color: #38bdf8; }

        /* RISK TAGS */
        .tag { padding:4px 10px; border-radius:6px; font-size:10px; font-weight:700; display: inline-block; }
        .tag-login { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }
        .tag-normal { background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid rgba(34, 197, 94, 0.3); }
        .tag-warning { background: rgba(234, 179, 8, 0.2); color: #fbbf24; border: 1px solid rgba(234, 179, 8, 0.3); }

        .status-pill { display: flex; align-items: center; font-size: 12px; color: #4ade80; background: rgba(34, 197, 94, 0.1); padding: 5px 12px; border-radius: 20px; }
        .dot { height: 8px; width: 8px; background: #22c55e; border-radius: 50%; margin-right: 8px; animation: pulse 2s infinite; }
        @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); } 70% { box-shadow: 0 0 0 10px rgba(34, 197, 94, 0); } 100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); } }
    </style>
</head>
<body>

<div class="header">
    <h1>PEHCHAAN AI <small style="font-size: 10px; color: #64748b; font-weight: 300;">V1.0.4</small></h1>
    <div class="status-pill"><span class="dot"></span> ENGINE ONLINE</div>
</div>

<div class="container">
    <div class="sidebar">
        <h3>Intelligence Filters</h3>
        <div class="filter active" onclick="setFilter('all', this)">All Activities</div>
        <div class="filter" onclick="setFilter('login', this)">Login Detection</div>
        <div class="filter" onclick="setFilter('media', this)">YouTube / Media</div>
        <div class="filter" onclick="setFilter('vapt', this)">VAPT / Vulnerable</div>
        <div class="filter" onclick="setFilter('search', this)">Google Searches</div>
    </div>

    <div class="main">
        <div class="cards">
            <div class="card"><h2 id="stat-total">0</h2><span>TOTAL EVENTS</span></div>
            <div class="card"><h2 id="stat-login" style="color: #f87171;">0</h2><span>LOGIN ATTEMPTS</span></div>
            <div class="card"><h2 id="stat-warning" style="color: #fbbf24;">0</h2><span>WARNINGS</span></div>
            <div class="card"><h2 id="stat-sessions" style="color: #4ade80;">1</h2><span>ACTIVE SESSIONS</span></div>
        </div>

        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th width="12%">Timestamp</th>
                        <th width="35%">Activity Title</th>
                        <th width="40%">Source URL</th>
                        <th width="13%">Risk Level</th>
                    </tr>
                </thead>
                <tbody id="log-table"></tbody>
            </table>
        </div>
    </div>
</div>

<script>
    let currentFilter = 'all';

    function setFilter(type, element) {
        currentFilter = type;
        $('.filter').removeClass('active');
        $(element).addClass('active');
        updateDashboard(); // Instant update on click
    }

    function updateDashboard() {
        $.getJSON('/api/logs', function(data) {
            // Update Stats
            $('#stat-total').text(data.length);
            $('#stat-login').text(data.filter(l => l.url.includes('login') || l.title.toLowerCase().includes('login')).length);
            $('#stat-warning').text(data.filter(l => l.url.includes('vapt') || l.url.includes('vuln')).length);

            let filteredData = data;

            // Apply Sidebar Logic
            if (currentFilter === 'login') {
                filteredData = data.filter(l => l.url.includes('login') || l.title.toLowerCase().includes('login'));
            } else if (currentFilter === 'media') {
                filteredData = data.filter(l => l.url.includes('youtube.com') || l.url.includes('netflix.com'));
            } else if (currentFilter === 'vapt') {
                filteredData = data.filter(l => l.url.includes('vapt') || l.url.includes('vuln') || l.url.includes('exploit'));
            } else if (currentFilter === 'search') {
                filteredData = data.filter(l => l.url.includes('google.com/search'));
            }

            let rows = '';
            filteredData.slice().reverse().forEach(function(log) {
                let isLogin = log.url.includes('login') || log.title.toLowerCase().includes('login');
                let isWarning = log.url.includes('vapt') || log.url.includes('vuln');
                
                let tag = '<span class="tag tag-normal">NORMAL</span>';
                if (isLogin) tag = '<span class="tag tag-login">LOGIN</span>';
                else if (isWarning) tag = '<span class="tag tag-warning">WARNING</span>';

                rows += `<tr>
                    <td>${log.time}</td>
                    <td><strong style="color: #e2e8f0">${log.title}</strong></td>
                    <td><a href="${log.url}" target="_blank" class="url-link">${log.url}</a></td>
                    <td>${tag}</td>
                </tr>`;
            });
            $('#log-table').html(rows);
        });
    }

    setInterval(updateDashboard, 1500);
</script>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/logs')
def get_logs():
    return jsonify(activity_logs)

@app.route('/log', methods=['POST'])
def log_endpoint():
    data = request.get_json()
    if data:
        data['time'] = datetime.now().strftime("%H:%M:%S")
        if not activity_logs or activity_logs[-1]['url'] != data['url']:
            activity_logs.append(data)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "failed"}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)