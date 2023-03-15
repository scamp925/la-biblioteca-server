# User Deletes Their Review in the Database

### Endpoint

*Note: The '12' in my endpoint and in the snippet from Postman was the id of the review I created with the [POST request](/CreateReview.md). Where I have '12', put the value of the id property of your newly created entry in Review table.*

```
http://localhost:8000/reviews/12
```


### Postman Response

HTTP response status code: 204 No Content

### What Happened to La Biblioteca's SQLite Database??

Entry with the ID of 12 in Reivew table has been permanently deleted from table

<table><tr?></tr><td valign="top" width=50%>
Before:

![database snippet of added entry](https://user-images.githubusercontent.com/98675776/225180104-15eba47d-ccdb-4632-bbf8-616590e5f911.png)
</td><td valign="top" width=50%>
After:

![database snippet of deleted entry](https://user-images.githubusercontent.com/98675776/225180282-25d95e65-fe48-42a7-9b78-e530297a9780.png)
</td></tr></table>
