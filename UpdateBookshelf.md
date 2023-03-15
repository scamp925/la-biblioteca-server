# User Updates Book's Shelf in the Database

### Endpoint & Body

http://localhost:8000/books/16/update_shelf?user=1

Here's how your Postman should look for this request:

![Postman setup for this call](https://user-images.githubusercontent.com/98675776/225177763-b10d6303-2c2f-4cdf-9349-632c7608a451.png)


### Postman Response

HTTP response status code: 204 No Content

![Postman Response Snippet](https://user-images.githubusercontent.com/98675776/225177810-66f3bf2e-f2a6-4d75-97eb-aa8ce2c9b96e.png)

### What Happened to La Biblioteca's SQLite Database??

<table><tr?></tr><td valign="top" width=50%>
Before:

![database snippet of added entry](https://user-images.githubusercontent.com/98675776/225176953-f94c5366-6b43-4050-9ab6-628efea28195.png)
</td><td valign="top" width=50%>
After:

![database snippet of updating an entry](https://user-images.githubusercontent.com/98675776/225177998-c026fb6c-cbea-4876-b653-44992e765bb7.png)
</td></tr></table>

### Usage in La Biblioteca's Client Side
Fetch API with this endpoint
- placeholder
