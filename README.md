# La Biblioteca: Server Side

[Walkthrough Video of La Biblioteca (3 mins)](https://www.loom.com/share/a18b70cc76444b25a73f45a6afb99fd0)

[Walkthrough Video with ME for La Biblioteca (5 mins)](https://www.loom.com/share/a18b70cc76444b25a73f45a6afb99fd0)

![La-Biblioteca](https://media.licdn.com/dms/image/C4E22AQHcSRSwmXmBBw/feedshare-shrink_800/0/1676755433329?e=1681948800&v=beta&t=eCcaJAe1YdkN7Yzx_ziP7ehsoz3PhRsbSK0iKn44fIo)

## Topics
- [Project Overview](#project-overview)
- [Try La Biblioteca Out](#try-plated-out)
- [Testing Endpoints](#testing-endpoints-with-postman)
- [Planning for La Biblioteca](#planning-for-plated)
- [Tech Stacks for La Biblioteca](#tech-stacks)

## Project Overview
Welcome to my full stack capstone project for Nashville Software School!!

La Biblioteca is my version of one of my favorite websites, GoodReads. I enjoy so much about GoodReads, but, for me, there's one thing missing: the ability to rate finished books with full and half star ratings. For La Biblioteca users, the restraint of only rating books with full stars is gone, because let's be honest, some books are 4.5 stars and not 5 stars nor are they 4 stars. Now, fair ratings are giving AND La Biblioteca users still enjoy GoodReads features like placing books onto "Want to Read", "Currently Reading", and "Read" shelves, leaving a review of a read book, perusing other user's reviews, reacting to reviews and using the search bar to find either a book or an author.

[Scroll to top](#la-biblioteca-server-side)
## Try La Biblioteca Out
*You've found my server side repo. Yahoo! You can check out my client side repo [here](https://github.com/scamp925/la-biblioteca-client). Instructions on how to get the frontend on your local machine can be found in the repo's ReadMe.*

### How to run backend locally

1. Clone La Biblioteca server to your machine
``` bash
git clone git@github.com:scamp925/la-biblioteca-server.git
```
2. Move into Directory
``` bash
cd la-biblioteca-server
```
2. Install Packages & Setup Virtual Environment
``` bash
 pipenv install
```
``` bash
 pipenv shell
```

4. Make Migrations
``` bash
python manage.py makemigrations bibliotecaapi
```

``` bash
python manage.py migrate
```
5. Seed the Database

    *In your terminal, run following commands one at a time*

``` bash
python manage.py loaddata users
```

``` bash
python manage.py loaddata shelves
```

``` bash
python manage.py loaddata books
```

``` bash
python manage.py loaddata books_on_shelves
```

``` bash
python manage.py loaddata reactions
```

``` bash
python manage.py loaddata reviews
```

``` bash
python manage.py loaddata review_reactions
```

6. Start the API server
``` bash
python manage.py runserver
```

[Scroll to top](#la-biblioteca-server-side)

## Testing Endpoints with Postman

### Books
[GET All Books](/AllBooks.md)

[GET All User's Books](/AllUserBooks.md)

[GET Single Book](/SingleUserBook.md)

[POST Add Book to Shelf (CUSTOM ACTION)](/AddBookToShelf.md)

[PUT Update Book's Shelf (CUSTOM ACTION)](/UpdateBookshelf.md)

[DELETE Remove Book from Shelf (CUSTOM ACTION)](/RemoveBookFromShelf.md)

### Reviews

[GET All Reviews of Book](/AllBookReviews.md)

[GET Single Review of Book](/SingleBookReview.md)

[POST Create Review of Book]()

[PUT Update Review of Book]()

[DELETE Delete Single Review]()

[POST Create Reaction for Review (CUSTOM ACTION)]()

[DELETE Remove Reaction from Review (CUSTOM ACTION)]()

### Reactions

[GET All Review's Reactions]()

## Planning

#### La Biblioteca's MVP Wireframe
[Link to Wireframe](https://www.figma.com/file/oncaUqtr0mQdBfu6hlQipX/La-Biblioteca-MVP?node-id=0%3A1&t=soWRyWsgYsPn8Ejm-1)

#### La Biblioteca's MVP ERD
![image](https://user-images.githubusercontent.com/98675776/224432440-3f8e8266-5941-46dc-871d-b2cc374fadc6.png)


[Scroll to top](#la-biblioteca-server-side)
## Tech Stacks
### Backend
<div align="center"> 
<a href="https://www.python.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="50" /></a>  
<a href="https://www.djangoproject.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/django-original.svg" alt="Django" height="50" /></a>  
<a href="hhttps://www.sqlite.org/index.html" target="_blank"><img style="margin: 10px" src="https://user-images.githubusercontent.com/33158051/103467186-7b6a8900-4d1a-11eb-9907-491064bc8458.png" alt="SQLite" height="50" /></a>
</div>
<ul>
<li>Fixtures</li>
<li>ORM & SQL Queries</li>
<li>Models</li>
<li>API Endpoint Views</li>
<li>User authentication using authtoken</li>
<li>URL routing & action decorators</li>
</ul>

[Scroll to top](#la-biblioteca-server-side)
