# Get All Books in the Database

### Endpoint

http://localhost:8000/books

### Postman Response

HTTP response status code: 200 OK

A list of 40 books with their details (see snapshot below for reference)

*Note: The Bookshelf property initial state is an empty string. When a book is placed on a shelf, the shelf name will be the value. Check out that endpoint [here](/SingleUserBook.md)*

![All Books Data](https://user-images.githubusercontent.com/98675776/225170060-26946b77-63ac-4a20-a8d9-4fddad689c0b.png)

### Usage in La Biblioteca's Client Side
Fetch API with this endpoint
- renders all books on the homepage of the application once a user is logged in
- the key to how the search bar filters the books on the page based on what the user inputs
