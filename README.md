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

Search all existing categories.

### Request
`GET /v1/categories`

Example:

```json

```

Get one category
`GET /v1/categories/{id}`

Get most recent items from a category

`GET /v1/categories/{id}/popular`


## Items

Get an item.

`GET /v1/items/{id}`

Create an item
### Request

`POST /v1/items`

Get an item.

### Request
`GET /v1/items/{id}`

### Response

On success, response body contains an array of objects. If no matches are found, an empty array is returned.

On error, the header status code is an error code and the response body contains an error object.

Example:

```json

```
