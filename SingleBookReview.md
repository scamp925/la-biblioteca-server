# Get Single Review from the Database

### Endpoint

```
http://localhost:8000/reviews/1
```

### Postman Response

HTTP response status code: 200 OK


```
{
    "id": 1,
    "star_rating": 100,
    "content": "This is a book to treasure, a new classic. I absolutely loved it.",
    "created_on": "2008-03-01",
    "book": {
        "id": 1,
        "title": "The Book Thief",
        "author": "Markus Zusak",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1522157426i/19063.jpg",
        "description": "It is 1939. Nazi Germany. The country is holding its breath. Death has never been busier, and will be busier still. By her brother's graveside, Liesel's life is changed when she picks up a single object, partially hidden in the snow. It is The Gravedigger's Handbook, left behind there by accident, and it is her first act of book thievery. So begins a love affair with books and words, as Liesel, with the help of her accordian-playing foster father, learns to read. Soon she is stealing books from Nazi book-burnings, the mayor's wife's library, wherever there are books to be found. But these are dangerous times. When Liesel's foster family hides a Jew in their basement, Liesel's world is both opened up, and closed down.In superbly crafted writing that burns with intensity, award-winning author Markus Zusak has given us one of the most enduring stories of our time.",
        "length": 552,
        "first_published": "2006-03-01"
    },
    "user": {
        "id": 2,
        "first_name": "Benito Antonio",
        "last_name": "Martínez Ocasio",
        "profile_image": "https://images.squarespace-cdn.com/content/v1/591b5715725e257ade2cc691/1628621930018-6P5FC55O941O6ZRNECOY/bb.jpg?format=1000w",
        "nickname": "Bad_Bunny",
        "created_on": "2023-01-15",
        "active": true,
        "uid": "lgofdh1987"
    }
}
```
