# jbl-chat

This is a simple chat application built with Django and HTMX.

## About

This is a simple real-time chat application built with Django and HTMX. While it
provides basic messaging functionality, it is not intended to be a full-featured
chat platform.

Messages cannot be edited or deleted, and private chats are not supported.
Additionally, new user registration is not yet available. To create an account,
you must use the Django admin interface or the Django shell.

This project was developed by Humberto Alves as part of a hiring process to
demonstrate how to build a real-time chat application with Django and HTMX.

Log in and start chatting! 🚀

## Default Users

The following users are available by default:

| Username | Password | Superuser | Staff |
|----------|----------|-----------|-------|
| anna     | dRBo1HzN | Yes       | Yes   |
| bob      | dRBo1HzN | No        | No    |
| charlie  | dRBo1HzN | No        | No    |

## API

The API is available at `/api/`. It provides the following endpoints:

- `GET /api/users/`: List all users.
- `GET /api/users/me/`: Retrieve the current user.
- `GET /api/users/<username>/`: Retrieve a user by ID.
- `GET /api/chats/`: List all chats.
- `GET /api/chats/<username>/`: Retrieve a chat by username.
- `GET /api/chats/<username>/messages/`: List all messages in a chat.
- `POST /api/chats/<username>/messages/`: Create a new message in a chat.

There is more information about the API in the built-in documentation at
`/api/`.

## Original README

Let's set the stage, you are the founder of this exciting new messaging startup,
you are tasked with building the first version of a product that is aimed to
evolve with feedback from the team and users.

You're building the backend using Django, and your initial task is to expose a
starting API while also leveraging HTMX for interactive front-end experiences.
With this first release, we want to deliver the following user stories:

1. As a user, I want to see all other users on the platform.
2. As a user, I want to view my conversation with another user.
3. As a user, I want to be able to send messages to another user on the
   platform.

Given that this is your startup, you have the freedom to set up and utilize the
practices that align with your goals. You can use any Python libraries or
external tools that you prefer.

We have provided a Django skeleton project along with Docker setup for your
convenience. Feel free to utilize Docker for development or Python virtual
environments for your local setup. Since managing user registration isn’t
required for this assessment, you can create dummy users directly using the
shell and implement session authentication for the API.

Incorporating HTMX will allow you to create dynamic, interactive elements on the
front end without needing to reload the page. We encourage you to think about
how HTMX can enhance user interactions effectively.

Please submit your solution as a pull request to our public repository. Happy
coding!
