# Get All of User's Books in the Database

### Endpoint

http://localhost:8000/books?user=1

### Postman Response

HTTP response status code: 200 OK

A list of 40 books with their details, but this time the property called "book_shelf" now lists what shelf this specific user has a book (see snapshot below for reference). 

*If book is not on user's bookshelves, then the "book_shelf" property's value will remain as an empty string*

![All Books Data](https://user-images.githubusercontent.com/98675776/225172905-6e5b7dab-0d63-482e-b1de-1656e22ba82b.png)

### Usage in La Biblioteca's Client Side
Fetch API with this endpoint
- renders all books on the homepage of the application once a user is logged in
- the key to how the search bar filters the books on the page based on what the user inputs
