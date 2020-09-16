[![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# Django Auth Template

This template contains a project, `django_auth_template`, and an app, `api`,
which are set up complete with user authentication and an example resource,
`Mango`, which has an example user ownership implementation.

## Preparation

1. [Download](../../archive/master.zip) this template.
1. Move the .zip file to your `sei/projects/` directory and Unzip it (creating a
   folder) -- **NOTE:** if the folder was already unzipped, use the `mv` command
   line to move it to the `sei/projects/` directory.
1. Empty [`README.md`](README.md) and fill with your own content.
1. Move into the new project and `git init`.
1. Create and checkout to a new branch, `training`, for your work.
1. Create a `.env` file
1. Add a key `ENV` with the value `development` **exactly**.
    1. Note: When you deploy, you will create this key on Heroku the value `production`. This will distinguish the development and production settings set in this template.
1. Run `pipenv shell` to start up your virtual environment.
1. Run `pipenv install` to install dependencies.
2. Create a psql database for your project
    1. Edit `settings.sql` then run `psql -U postgres -f settings.sql`
    OR:
    1. Type `psql` to get into interactive shell.
    2. Run `CREATE DATABASE "project_db_name";` where `project_db_name` is the name you want for your database.
1. Add the database name to the `.env` file using the key `DB_NAME_DEV`.
1. Replace all instances of `django_auth_template` with your application name. **This includes the folder included in this repository.**
2. Generate a secret key using [this tool](https://djecrety.ir) and add it to the `.env` file using the key `SECRET`.
1. Open the repository in Atom with `atom .`

### The `.env` File

After following the steps above, your `.env` file should look _something_ like
the following, replacing `project_db_name` with your database name and
`secret_key` with your secret key.

```sh
ENV=development
DB_NAME_DEV=project_db_name
SECRET=secret_key
```

## Structure

This template includes a project `django_auth_template` which should be renamed
as part of the set-up steps. It includes the `settings.py` file with special
settings to be able to run both locally and on production. **DO NOT ADD A NEW
OR MODIFY THE CURRENT `DATABASES` DEFINITION UNLESS INSTRUCTED TO DO SO.**

There is also an app `api` which can be renamed if necessary. The `api` app
includes folders for models and view files, which can then be imported into
`urls.py` for use.

## Commands

Commands are run with the syntax `python3 manage.py <command>`:

| command | action |
|---------|--------|
| `runserver`  |  Run the server |
| `makemigrations`  | Generate migration files based on changes to models  |
| `migrate`  | Run migration files to migrate changes to db  |
| `startapp`  | Create a new app  |

## Debugging

`pipenv shell` moved me into a different directory!

> Pipenv wants to be in the root directory, so if it thinks it's not then it
> will move you to what it thinks is the root of your repository. Exit out
> of the shell with `exit`, then check if the folder it moved you to is a git
> repository. If you see a `.git` folder inside of the `trainings` folder,
> for example, delete that folder so that `trainings` is no longer a "git repo."
> Then, you can change back into your project directory and try running
> `pipenv shell` again.

`pipenv shell` is complaining about my python version not matching

> Our python version is defined in the `Pipfile`. Simply replace the current
> `python_version = "x.x"` statement with the appropriate version.

SyntaxError pointing to `manage.py` when trying to run the server, migrate, etc.

> Double-check your python version with `python --version`. If you see a "2.x.x"
> version, then you need to use the command `python3` when running python
> scripts. You can also follow these guides to replace your `python` command so
> it always uses python3.
>
> Mac: https://stackoverflow.com/questions/49704364/make-python3-as-my-default-python-on-mac/49711594
>
> Linux: https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux

Error: No module named <my-projects-name> when trying to run the server

> If Python can't find the module that is your project name, then very likely
> you forgot a very important piece of the preparation steps. You need to
> make sure you rename the project folder as well.

I made changes to my models & ran my migrations but it says "No migrations to apply"

> Double-check that you **generated** the migration files before you tried
> to run them. This means running `makemigrations` before `migrate`.

Errors with `psycopg2`

> There's a lot to read about this issue if you want:
> https://github.com/psycopg/psycopg2/issues/674
> https://www.psycopg.org/articles/2018/02/08/psycopg-274-released/
>
> This template uses `psycopg2-binary` to minimize errors during project
> development. If you have errors with `psycopg2` anyway, notify an instructor.

## Deployment

Before deploying, make sure you have renamed your project folder and replaced
all instances of `django_auth_template` with your app's name.

Once ready, you can follow the steps in the [django-heroku-deployment-guide](https://git.generalassemb.ly/ga-wdi-boston/django-heroku-deployment-guide).

## Additional Resources

- [Django Rest Framework Tutorial: Authentication](https://www.django-rest-framework.org/api-guide/authentication)

## [License](LICENSE)

1.  All content is licensed under a CC­BY­NC­SA 4.0 license.
1.  All software code is licensed under GNU GPLv3. For commercial use or
    alternative licensing, please contact legal@ga.co.
