### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
JavaScript is client side and python is server side. Python uses snake case and JS uses camel case. Python is very dynamic and high level. Much more automated then JS. Python uses indetation rather than {} to show blocks of code. 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  get(key,def_value)
  setdefault(key, def_value)

- What is a unit test?
Testing of one unit or part, usually a function or a method

- What is an integration test?
Testing of how things work together. Example I remember was the sliding door with the lock, yes it locks the door but the door slides right out of the lock due to it being opened a different way then it was locked. So testing that functions work together and not work separately but not solve the problem. 

- What is the role of web application framework, like Flask?
They are to handle web requests, produce dynamic HTML, handle forms, handle cookies, connect to databases, provide user log-in/log-out, cache pages for performance. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
should use a URL Parameter when it feels more like "subject of page" and Query Parameter when it feels more like "extra info about page" often used when coming from a form submitted by the client. 

- How do you collect data from a URL placeholder parameter using Flask?
flask lets you "route" a URL to a function with a decorator of @app.route("/whatever") to produce the html response of that page using a function. 

- How do you collect data from the query string using Flask?
by using request.args which is a dictionary-like object of query parameters collected from the user

- How do you collect data from the body of the request using Flask?
by submitting a request to the flask server and returning the information requested from the the function

- What is a cookie and what kinds of things are they commonly used for?
cookies are name value pairs that are stored by the client. Example given was if there is an alert that the user has removed a cookie will remember that when it moves from page to page.  Cookies are a key value pair stored by the client browser. The server tells client to store these. The client sends cookies to the server with each request. Cookie information is sent via a header to the server. Is someone logged in? What’s their username.

- What is the session object in Flask?
it is stored in the browser as a cookie and they are signed so users can see but they can't change their actual session data. 

- What does Flask's `jsonify()` do?
Will send a JSON reponse to the browser
