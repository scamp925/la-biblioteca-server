# User Adds Reaction to a Review in the Database

### Endpoint & Body

```
http://localhost:8000/reviews/7/add_reaction
```

Here's how your Postman should look for this request:

![Postman setup for this call](https://user-images.githubusercontent.com/98675776/225180600-ae291d5f-345a-4f6f-9cf4-6d37324e4791.png)


### Postman Response

HTTP response status code: 201 CREATED

![Postman Response Snippet](https://user-images.githubusercontent.com/98675776/225180638-a71d470c-70d0-46e3-889d-81fca80c9fec.png)

### What Happened to La Biblioteca's SQLite Database??

A new entry in the ReviewReaction table:

*Note: The id value for your newly created ReviewReaction will most likely differ from the one in the response snippet below*

![database snippet of added entry](https://user-images.githubusercontent.com/98675776/225180750-9c1b9350-972b-435d-af1e-2281e1959d5a.png)

### Usage in La Biblioteca's Client Side
Fetch API with this endpoint
- placeholder
