# Food Forest

A web application that detects the name of the input food image and lists down its ingredients along with their nutritional values. The web application uses Django for the backend and Bootstrap stying for the frontend.

## Setup & Run

First, create a virtual environment and install the required dependencies using the `requirements.txt` file to run the application. Follow the steps ahead.

```shell
virtualenv environment # Creates a virtual environment
environment\Scripts\activate # Switches to the virtual environment
pip install -r requirements.txt # Installs the dependencies
```

Next, to run the web application, use the following command to start the server and redirect to `http://127.0.0.1:8000` to use the web application.

```shell
python manage.py runserver # Starts the server
```

## Database

The `db.sqlite3` file contains the following tables.
  * `core_food`: This table contains information about the food categories.
  * `core_ingredient`: This table contains information about the food ingredients.
  * `core_recipe`: This is an intermediary table that maps food materials with ingredients.

There are several other tables that are Django specific and are not related to the project.
