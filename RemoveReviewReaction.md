# User Removes Reaction from Review in the Database

### Endpoint & Body

*Note: The '7' in my endpoint and in the snippet from Postman was the id of the ReviewReaction I created with the [POST request](/AddReviewReaction.md). Where I have '7', put the value of the id property of your newly created entry in ReviewReaction table.*

```
http://localhost:8000/reviews/7/remove_reaction
```

Here's how your Postman should look for this request:

![Postman setup for this call](https://user-images.githubusercontent.com/98675776/225180860-14d4f11f-36b3-4180-90af-e86c95c751b1.png)


### Postman Response

HTTP response status code: 204 No Content

### What Happened to La Biblioteca's SQLite Database??

Entry with the ID of 7 in Bookshelf table has been permanently deleted from table

<table><tr?></tr><td valign="top" width=50%>
Before:

![database snippet of added entry](https://user-images.githubusercontent.com/98675776/225180750-9c1b9350-972b-435d-af1e-2281e1959d5a.png)
</td><td valign="top" width=50%>
After:

![database snippet of deleted entry](https://user-images.githubusercontent.com/98675776/225180953-2f963d6a-44eb-4941-a6b5-b09627423f46.png)
</td></tr></table>
