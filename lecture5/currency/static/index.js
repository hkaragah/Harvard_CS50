document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#form').onsubmit = () => {

        // Initialize new request
        const request = new XMLHttpRequest(); // XMLHttpRequest object to request data from a web server
        const currency = document.querySelector('#currency').value; 
        request.open('POST', '/convert'); // POST request to /convert route, it say where to send the request to. The "current" still need to be added to this request.   
        
        // Callback function for when request completes (what to do when the request is done)
        request.onload = () => {

            // Extract JSON data from request (JSON is a built-in JavaScript object that can be used to convert data to and from JSON)
            const data = JSON.parse(request.responseText);

            // Update the result div
            if (data.success) {
                console.log(data.success);
                const contents = `1 USD is equal to ${data.rate} ${currency}.`
                document.querySelector('#result').innerHTML = contents;
            } else {
                console.log(data.success);
                document.querySelector('#result').innerHTML = 'There was an error.';
            }
        }

        // Add data to send with request
        const data = new FormData();
        data.append('currency', currency);

        // Send request
        request.send(data);
        return false;
    }
});