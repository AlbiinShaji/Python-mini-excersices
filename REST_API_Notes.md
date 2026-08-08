# REST API Concept Notes

## 1. What is REST?

REST (**RE**presentational **S**tate **T**ransfer) is an architectural style for designing networked applications. A REST API lets a client (browser, mobile app, another service) communicate with a server over HTTP using a standard, predictable set of rules.

Core principles:
- **Client-server**: client and server are separate; either can evolve independently.
- **Stateless**: every request from the client contains all the information the server needs. The server does not store client session state between requests.
- **Uniform interface**: resources are accessed and manipulated using a consistent set of operations (HTTP methods) and a consistent addressing scheme (URLs).
- **Resource-based**: everything is modeled as a "resource" (e.g. a user, an order, a product), identified by a URL, like `/users/5`.
- **Representations**: the client and server exchange representations of resources, usually as JSON.

## 2. HTTP Methods

| Method | Purpose | Example |
|---|---|---|
| `GET` | Retrieve a resource or list of resources | `GET /users` → list all users |
| `POST` | Create a new resource | `POST /users` → create a new user |
| `PUT` | Replace a resource entirely | `PUT /users/5` → replace user 5's data |
| `PATCH` | Partially update a resource | `PATCH /users/5` → update just one field |
| `DELETE` | Remove a resource | `DELETE /users/5` → delete user 5 |

## 3. Idempotency & Safety

- **Safe methods** don't change server state: `GET`.
- **Idempotent methods** produce the same result no matter how many times you call them: `GET`, `PUT`, `DELETE`.
- **Non-idempotent**: `POST` (calling it twice creates two resources).

## 4. HTTP Status Codes

| Range | Meaning | Common codes |
|---|---|---|
| 2xx | Success | `200 OK`, `201 Created`, `204 No Content` |
| 3xx | Redirection | `301 Moved Permanently` |
| 4xx | Client error | `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found` |
| 5xx | Server error | `500 Internal Server Error` |

## 5. Request/Response Structure

A typical request has:
- **Method** (`GET`, `POST`, etc.)
- **URL/endpoint** (e.g. `/api/users/5`)
- **Headers** (metadata like `Content-Type: application/json`, `Authorization: Bearer <token>`)
- **Body** (optional, usually JSON — used for `POST`/`PUT`/`PATCH`)

A typical response has:
- **Status code** (e.g. `200`, `404`)
- **Headers**
- **Body** (usually JSON representing the resource or an error message)

Example JSON body:
```json
{
  "id": 5,
  "name": "Alby",
  "role": "Intern"
}
```

## 6. Endpoints & Resource Naming

Good REST APIs use nouns, not verbs, and represent hierarchy through the URL:

```
GET    /users          -> list users
POST   /users          -> create a user
GET    /users/5        -> get user 5
PUT    /users/5        -> replace user 5
PATCH  /users/5        -> update part of user 5
DELETE /users/5        -> delete user 5
GET    /users/5/orders -> list orders belonging to user 5
```

## 7. Example: Simple REST Endpoint in Flask

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    1: {"name": "Alby", "role": "Intern"}
}

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_id = max(users.keys()) + 1
    users[new_id] = data
    return jsonify(users[new_id]), 201

if __name__ == "__main__":
    app.run(debug=True)
```

This shows:
- Reading a resource with `GET` and returning a `404` if it's missing.
- Creating a resource with `POST`, reading the JSON body via `request.get_json()`, and returning `201 Created`.

## 8. Statelessness in Practice

Since REST APIs are stateless, authentication info (like a token) must be sent with *every* request — typically in the `Authorization` header — rather than relying on the server remembering who's logged in from a previous request.

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

## Summary

REST is a way of structuring APIs around resources, using standard HTTP methods and status codes so that any client can predictably interact with any REST-compliant server without needing custom rules per API.
