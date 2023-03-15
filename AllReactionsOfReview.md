# Get All Reactions of a Single Review in the Database

### Endpoint

```
http://localhost:8000/reactions?review=7
```

### Postman Response

HTTP response status code: 200 OK

A list of all the reactions associated with single review with an id of 7

```
[
    {
        "id": 1,
        "label": "Raised Hands",
        "image_url": "https://a.slack-edge.com/production-standard-emoji-assets/14.0/google-medium/1f64c.png",
        "reaction_clicked": false,
        "reaction_count": 0
    },
    {
        "id": 2,
        "label": "Love",
        "image_url": "https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/2764-fe0f.png",
        "reaction_clicked": false,
        "reaction_count": 0
    },
    {
        "id": 3,
        "label": "Face With Raised Eyebrow",
        "image_url": "https://a.slack-edge.com/production-standard-emoji-assets/14.0/google-medium/1f928.png",
        "reaction_clicked": true,
        "reaction_count": 1
    }
]
```
