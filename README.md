# url-shortener
test app for url shortener


## setup python virtual environment using venv
```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install requests
pip install psycopg2
pip freeze > requirements.txt
```

## setup postgres locally
```bash
#install postgres on MAC
brew install postgres
# check postgres 
postgres --version
#start postgres
initdb /usr/local/var/postgres
pg_ctl -D /usr/local/var/postgres start
#stop postgres
pg_ctl -D /usr/local/var/postgres stop
#create a test db
createdb test_db
#to drop a database
dropdb test_db
#export connection string
export TEST_DB='postgres://bapi@localhost/test_db?connect_timeout=5&sslmode=disable'
```

## setup tables in postgres
Log into the `test_db` we setup locally and setup tables from `ddl.sql`
```bash
$ psql $TEST_DB
```

## Running the app
* Open terminal and goto the directory where the app is located
* Activate python virtual environment using `source venv/bin/activate`
* Install the requirements using `pip install -r requirements.txt`  
* Run the flask application using `flask run` or run python script using `python3 app.py`
* To test it we can use following example



