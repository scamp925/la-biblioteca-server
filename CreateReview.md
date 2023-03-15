# User Adds a Review to a Book in the Database

### Endpoint & Body

```
http://localhost:8000/reviews
```

Here's how your Postman should look for this request:

![Postman setup for this call](https://user-images.githubusercontent.com/98675776/225179350-ffbb8e48-388a-4066-b3cd-3685896d4728.png)


### Postman Response

HTTP response status code: 201 CREATED

*Note: The id value for your newly created review will most likely differ from the one in the response snippet below*
```
{
    "id": 12,
    "star_rating": 50,
    "content": "",
    "created_on": "2023-02-19",
    "book": {
        "id": 16,
        "title": "Dracula",
        "author": "Bram Stoker",
        "cover_image": "https://img.thriftbooks.com/api/images/m/3319309c8c50896c2b8017d87a36734342852aee.jpg",
        "description": "Dracula is an 1897 Gothic horror novel by Irish author Bram Stoker.Famous for introducing the character of the vampire Count Dracula, the novel tells the story of Dracula's attempt to move from Transylvania to England so he may find new blood and spread undead curse, and the battle between Dracula and a small group of men and women led by Professor Abraham Van Helsing. Dracula has been assigned to many literary genres including vampire literature, horror fiction, the gothic novel and invasion literature. The novel touches on themes such as the role of women in Victorian culture, sexual conventions, immigration, colonialism, and post-colonialism. Although Stoker did not invent the vampire, he defined its modern form, and the novel has spawned numerous theatrical, film and television interpretations.",
        "length": 488,
        "first_published": "1897-05-26"
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
