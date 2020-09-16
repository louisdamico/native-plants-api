# Application: Native Plant Species Field App

This application is a Native plant field guide designed for professionals and a DIYer of all levels.  The simplicity of the list, along with easy to use navigation will be an asset for users in an outdoor environment. Each user will be able to search by state and ecoregion to find which plant species is native to their particular area. Once they choose a location, the database will populate a list of native species for different categories; Trees, Shrubs, Plants, Flowers, Grasses, etc...  Each one will have a Picture of the species, and description and an average price.  The user then can pick their favorite ones and add it to a Client/favorite list for future reference.

## Important Links

- [Deployed Client]
- [Client Repo]https://louisdamico.github.io/native-plants-client/
- [Deployed API]
- [Gantt Chart](https://docs.google.com/spreadsheets/d/1hUHYbxF8i37bEgrGfgN9qWebLXFGVB-AdIgRZn4mn1o/edit?usp=sharing)

## Planning Story



### User Stories

- As an unregistered user, I would like to sign up with email and password.
- As a registered user, I would like to sign in with email and password.
- As a signed in user, I would like to change password.
- As a signed in user, I would like to sign out.
- As a signed in user, I would like to choose my state.
- As a signed in user, I would like to pick a local region
- As a signed in user, I would like to search for a native plant in different categories.
- As a signed in user, I would like to view the details from selected species.
- As a signed in user, have the option to store my choices to client/favorites list.
- As a signed in user, be able to delete from my client/favorites list.

### Strech Goal(s)

- Allow users to comment on comments.


### Technologies Used

- Python
- Django
- ProsgreSQL

### Catalog of Routes

| Verb   | URI Pattern            |
|--------|------------------------|
| POST   | `/posts/:id/comments`  |
| PATCH  | `/posts/:id/comments/:commentid` |
| DELETE | `/posts/:id/comments/:commentid` |
| GET      | `/posts`        |
| GET      | `/posts/:id`|
| POST     | `/posts`|
| PATCH    | `/posts/:id`|
| DELETE  | `/posts/:id`|



### Unsolved Problems

- Still need style the overall look and feel of the application
- Would like to eventually add a home page that renders all posts so unauthenticated users can view all posts.

## Images

#### ERD:
<a href="https://imgur.com/fMLv2Jv"><img src="https://i.imgur.com/fMLv2Jv.png" title="source: imgur.com" /></a>
