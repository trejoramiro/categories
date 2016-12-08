# Athletic Catalog
![Athletic Catalog](https://c3.staticflickr.com/6/5141/30169964986_daa41bf577_m.jpg)
## About Athletic Catalog

Created by: Ramiro Trejo

## Watch Demo
Coming Soon.

### Techstack
#### Front-End
Bootstrap

#### Back-End
Flask

SQLite

# API Endpoint Reference

## Categories

Return all categories.

`GET /v1/categories`

Get one category.

`GET /v1/categories/{id}`

Create a category.

`POST /v1/categories`

| Query Parameter | Value |
|---|---|
|  name | *Required.* |

Delete a category.

`DELETE /v1/categories/{id}`

Get all items from a category.

`GET /v1/categories/{id}/items`

Get most recent items from a category.

`GET /v1/categories/{id}/newest`

## Items

Get an item.

`GET /v1/items/{id}`

Create an item.

`POST /v1/items`

| Query Parameter | Value |
|---|---|
| name | *Required.* |
| category_id | *Required.* |
| description | *Optional.* |
| price | *Optional.* |

Update an item.

`PUT /v1/items`

Delete an item.
`DELETE /v1/items/{id}`

## Images

Get all images of an item.

`GET /v1/items/{id}/images`

Get an image from an item.

`GET /v1/items/{id}/images/{id}`

Save an image to an item.

`POST /v1/items/{id}/images`

| Query Parameter | Value |
|---|---|
| url | *Required.* |
| item_id | *Required.* |

Delete an image from an item.

`DELETE /v1/items/{id}/images`

## Stocks

Get the stock info. of an item.

`GET /v1/items/{id}/stock`

Create stock info. for an item.

`POST /v1/items/{id}/stock`

| Query Parameter | Value |
|---|---|
| quantity | *Required.* |
| item_id | *Required* |
|  color | *Optional.* |
| size | *Optional.*  |

Update the stock info. of an item.

`PUT /v1/items/{id}/stock`

Delete the stock info. of an item.

`DELETE /v1/items/{id}/stock`

## Reviews

Get all reviews of an item.

`GET /v1/items/{id}/reviews`

Get a review of an item.

`GET /v1/items/{id}/reviews/{id}`

Create a review for an item.

`POST /v1/items/{id}/reviews`

| Query Parameter | Value |
|---|---|
| rating | *Required.* |
| user_id | *Required.* |
| item_id | *Required.* |
|  body | *Optional.* |
