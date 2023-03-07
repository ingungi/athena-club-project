# athena-club-project
To run the Athena Club project locally, follow these steps:

Clone the project repository from GitHub using the following command:
bash
Copy code
git clone https://github.com/ingungi/athena-club-project.git
Create a virtual environment for the project and activate it. This can be done using the following commands:
bash
Copy code
python -m venv venv
source venv/bin/activate (for linux/mac)
venv\Scripts\activate (for windows)
Install the project dependencies using the following command in the project root directory:
Copy code
pip install -r requirements.txt
Create a PostgreSQL database and update the DATABASES configuration in settings.py file with your database details.

Run the database migrations using the following command in the project root directory:

Copy code
python manage.py migrate
Load the initial data into the database using the following command:
bash
Copy code
python manage.py loaddata fixtures/initial_data.json
Run the backend server using the following command in the project root directory:
Copy code
python manage.py runserver
Open another terminal window and navigate to the frontend directory.

Install the frontend dependencies using the following command:

Copy code
npm install
Run the frontend server using the following command in the frontend directory:
Copy code
npm run serve
Access the application by visiting http://localhost:8080 in your browser.
Note: The project uses environment variables for some configurations. Create a .env file in the project root directory and set the values for the following variables:

makefile
Copy code
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=your_database_host
DATABASE_PORT=your_database_port
