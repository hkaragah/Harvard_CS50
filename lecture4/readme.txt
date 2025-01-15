HTTP Methods:
- GET: retrieve resource
- POST: create a nmew resource
- PUT: replace a resource
- PATCH: update a resource
- DELETE: delete a resource


The "requests" library facilitate making the above requiests:
- requests.get(url)
- requests.post(url)
- requests.put(url)
- requests.patch(url)
- requests.delete(url)


HTTP requests status code:
- 200: OK
- 201: Created
- 400: Bad requests (e.g., ill-formatted)
- 403: Forbidden (e.g., access a resource that needs a special permission)
- 404: Not found (e.g., flight number not in the database)
- 405: Method not allowed (e.g., POST requets may notbe allowed on some APIs)
- 422: Unprocessable entity (e.g., ill-formatted)
- ...