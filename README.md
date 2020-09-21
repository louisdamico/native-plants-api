# Application: Native Plant Species Field App

This application is a Native plant field guide designed for professionals and a DIYer of all levels.  The simplicity of the list, along with easy to use navigation will be an asset for users in an outdoor environment. Each user will be able to search by state and ecoregion to find which plant species is native to their particular area. Once they choose a location, the database will populate a list of native species for different categories; Trees, Shrubs, Plants, Flowers, Grasses, etc...  Each one will have a Picture of the species, and description and an average price.  The user then can pick their favorite ones and add it to a Client/favorite list for future reference.

## Important Links

- [Deployed Client](https://louisdamico.github.io/record-collection-client/)
- [Client Repo]https://louisdamico.github.io/native-plants-client/
- [Deployed API](https://native-plants-app.herokuapp.com/)
- [Gantt Chart](https://docs.google.com/spreadsheets/d/1hUHYbxF8i37bEgrGfgN9qWebLXFGVB-AdIgRZn4mn1o/edit?usp=sharing)

## Planning Story

This application is designed to be a field list for anyone who wants a quick easy way to store and get info for their lists. It came to me when I was doing a native plant list for a commercial client a while back.  Trying to show a client a list of native plants, along with pictures and information about each one is a daunting task.  Lots of looking around at many different sites to get what you need.  So this will help streamline all the most popular resource sites for each region.
I started off with a loose idea of the layout, mainly wanted it easy with minimum user input for field use. Once I set up the database, I started working on getting a simple mock up in React and then I was ready to start coding!

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

- Allow users to choose their favorite plants by choosing a photo.
- Allow users to access all plant info from selected card.

### Technologies Used

- Python
- Django
- ProsgreSQL
- Node.js

## Set up and installation
1. Download this application.
2. Unzip the application.
3. Move into the folder.
4. If you're on MacOS, you can install Pipenv easily with Homebrew: `$ brew install pipenv`.
5. Run `pipenv shell` to start up your virtual environment.
6. Run `pipenv install` to install dependencies.
7. Run the back-end development server with `python3 manage.py runserver`.

### Catalog of Routes

| Verb   | URI Pattern            |  Controller#Action  |
|--------|------------------------|---------------------|
| POST   | `/sign-up`             | `users#signup`      |
| POST   | `/sign-in`             | `users#signin`      |
| DELETE | `/sign-out`            | `users#signout`     |
| PATCH  | `/change-password`     | `users#changepw`    |
| POST   | `/favorites-create`  |   `list#create`        |
| PATCH  | `/favorites-edit/:id` |  `list#edit`        |
| DELETE | `/favorites/:id` | `list#delete`   |
| GET      | `/favorites`|  `All list#retrieve` |
| GET      | `/favorites/:id`|  `list#retrieve` |

### Unsolved Problems

- Still need style the overall look and feel of the application
- Would like to eventually add more input fields.
- Us an API to pull all of the info for each element from a national database.

## Images

#### ERD:
<a href="https://imgur.com/fMLv2Jv"><img src="https://i.imgur.com/fMLv2Jv.png" title="source: imgur.com" /></a>
