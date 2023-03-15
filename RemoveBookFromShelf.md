# User Remove Book from Shelf in the Database

### Endpoint & Body

```
http://localhost:8000/books/16/remove_from_shelf
```

Here's how your Postman should look for this request:

![Postman setup for this call](https://user-images.githubusercontent.com/98675776/225178212-14ea9dba-be63-4dbf-b9c9-d151d1eea22b.png)


### Postman Response

HTTP response status code: 204 No Content

### What Happened to La Biblioteca's SQLite Database??

Entry with the ID of 7 in Bookshelf table has been permanently deleted from table

<table><tr?></tr><td valign="top" width=50%>
Before:

![database snippet of added entry](https://user-images.githubusercontent.com/98675776/225177998-c026fb6c-cbea-4876-b653-44992e765bb7.png)
</td><td valign="top" width=50%>
After:

![database snippet of updating an entry](https://user-images.githubusercontent.com/98675776/225178385-bf46ee70-d43a-4e33-a219-2fd35a2f36f7.png)
</td></tr></table>
