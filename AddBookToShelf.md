# User Adds Book to Shelf in the Database

### Endpoint & Body

http://localhost:8000/books/16/add_to_shelf

Here's how your Postman should look for this request:

![POST call](https://user-images.githubusercontent.com/98675776/225177070-f9e44b3c-2ecd-4e8a-91b6-f2557c07800a.png)


### Postman Response

HTTP response status code: 201 CREATED

![Postman Response Snippet](https://user-images.githubusercontent.com/98675776/225177137-6ba3b36e-ae13-492e-8e11-3f4363e6801f.png)

### What Happened to La Biblioteca's SQLite Database??

A new entry in the Bookshelf table:

![database snippet of added entry](https://user-images.githubusercontent.com/98675776/225176953-f94c5366-6b43-4050-9ab6-628efea28195.png)

### Usage in La Biblioteca's Client Side
Fetch API with this endpoint
- placeholder
