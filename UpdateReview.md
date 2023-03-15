# User Updates Book's Review in the Database

### Endpoint & Body

*Note: The '12' in my endpoint and in the snippet from Postman was the id of the review I created with the [POST request](/CreateReview.md). Where I have '12', put the value of the id property of your newly created review.*

```
http://localhost:8000/reviews/12
```

Here's how your Postman should look for this request:

![Postman setup for this call](https://user-images.githubusercontent.com/98675776/225179746-f091f11f-acfe-465a-a05d-c230d89eff36.png)


### Postman Response

HTTP response status code: 204 NO CONTENT


### What Happened to La Biblioteca's SQLite Database??


<table><tr?></tr><td valign="top" width=50%>
Before:

![database snippet of added entry](https://user-images.githubusercontent.com/98675776/225180001-2a41479b-84ed-48cf-9b1e-66709cd1aef0.png)
</td><td valign="top" width=50%>
After:

![database snippet of updating an entry](https://user-images.githubusercontent.com/98675776/225180080-af226185-eeb0-4a27-b563-f32e780e7ce2.png)
</td></tr></table>

Where the "content" was once empty, with the update, it is now filled with user's review
### Usage in La Biblioteca's Client Side
Fetch API with this endpoint
- placeholder
