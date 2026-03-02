chrome.tabs.onActivated.addListener(async info => {
    const tab = await chrome.tabs.get(info.tabId);
    send(tab);
});

chrome.tabs.onUpdated.addListener((id, change, tab) => {
    if (change.status === "complete") {
        send(tab);
    }
});

function send(tab) {
    if (!tab || !tab.url) return;
    if (tab.url.startsWith("chrome://")) return;

    fetch("http://127.0.0.1:5000/log", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            browser: "CHROME",
            title: tab.title || "",
            url: tab.url
        })
    });
}