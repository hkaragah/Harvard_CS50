Javascript Event:
- onclick
- onmouseover
- onkeydown
- onkeyup
- onload
- onblur (event occurs when an HTML element loses focus, event is often used on input fields)
- ...


Javascript querySelector:
- document.querySelector('tag')
- document.querySelector('#id')
- document.querySelector('.class')


Javascript Variables (most common):
- const (means a constant value, cannot re-assign it later)
- let (exist inside of the scope of the inner most curl braces surrounding it)
- var (simialr to let, but exist all the way inside of whatever function it was originally defined)


Arrow Functions (ES6 version of Javascript):

- Example of arrow function that takes no argument:

    () => {
        alert('Hello, world!');
    }

- Example of a function that takes a variable called "x":

    x => {
        alert(x);
    }

- Example of a function that takes an input and return a value almost right a way:

    x => x * 2


Ajax (Asyncronous Javascript and XML): 
- helps to get more information from a server even without needing to reload an entire new page

Socket.IO
- A Javascript library that lets us do real-time communication
- Modern web browsers support web sockets 
    which allow for a protocol that allow for 
    full-duplex communication between client and server 
    simultanously that allow for real-time communication

