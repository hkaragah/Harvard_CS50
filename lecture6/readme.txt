Jinja (Flask) and Django:
    - Use Jinja to embed code inside html (see "multipage")
    - Jinja (Flask) is a templating language used in Python web frameworks like 
      Flask and Django to create dynamic web pages.
    - Alternatively, you can use Django templates.

Single-Page vs. Multi-Page Apllications:
    -Advantage of single-apge app:
        The user stays on the same page anddoes not need to send 
        a new prequest each time (see  "singlepage0")
    -Disadvantage of single-page:
        The page url stays the same (see "singlepage0"). 
        There is turn-around (HTML5 History API) to recreate a new url for each link
        without the need to actually send a new request to the server (see "singlepage1").

HTML5 History API:
    A feature of HTML5 that allows us to manipulate the browser's history and
    update the url to reflect different urls that we might want to create.
    We can push url states into the web browser's history.
    -Disadvantage
        The back button does not work 
        because nothing in JS says what to when the back button is clicked.
        To fix it, we use another feature of HTML5 History API called "onpopstate".


Window:
    - window.innerWidth
    - window.innerHeight (the displayed portion)
    - window.scrolly (how far down along the page am I currently scorlled)


document:
    - document.body.offsetHeight (the entrie document height, not the displayed portion)
    - window.innerHeight + window.scrolly == document.body.offsetHeight 
        >>> I have scrolled to the bottom of the page