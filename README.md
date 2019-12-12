# Ambuj_Assignment


## Requirements

* Python (3.5 or above)
* Django (2.2 or above)

## Project setup:
* Open your command prompt/terminal, get inside your working directory. 

* Clone this repository `git clone https://github.com/ambujap94/Ambuj_Assignment.git`
     
* Change the directory to Ambuj_Assignment by  `cd Ambuj_Assignment`

* Install virtualenv in your system using the command `pip install virtualenv`.

* Create a virtual environment inside .venv folder `virtualenv .venv`

* Activate virtualenv 
    * `.\.venv\Scripts\activate ` (windows)
    * `source ./.venv/bin/activate` (Linux)

* Install all the requirements and dependencies using the requirement.txt `pip install -r requirements.txt`

* Run `migrate` to initilize database using `python manage.py migrate`

* Start the server using `python manage.py runserver`

## Unit Test:
  * Tests are written for GET and POT success and Post failure cases and can be checked by running a command 
  `python manage.py test`. Test cases were passed when cheked.
  
## Management Command ('fetch')

#### Run below management commands to import and valdate the data from AWS s3 via the API.

    * Tested Metrics are: Tmin, Tmax, Rainfall
    * Tested Locations are: England, Scotland, UK, Wales
#### Commands to run are `python manage.py fetch <Location> <Metric>`

```bash
python manage.py fetch England Tmin
python manage.py fetch England Tmax
python manage.py fetch England Rainfall
python manage.py fetch Scotland Tmin
python manage.py fetch Scotland Tmax
python manage.py fetch Scotland Rainfall
python manage.py fetch UK Tmin
python manage.py fetch UK Tmax
python manage.py fetch UK Rainfall
python manage.py fetch Wales Tmin
python manage.py fetch Wales Tmax
python manage.py fetch Wales Rainfall
```

### Note: It may take some time to fetch, insert and validate the data as data is a bit large.


## Testing Browsable API

Make sure server is running and open the below link in the browser
  http://127.0.0.1:8000/weatherdata
  
  ![image](https://user-images.githubusercontent.com/14863485/70658915-fc289400-1c84-11ea-8849-3d2dd3cbf7c8.png)

Now you can post data from the HTML form shown in the above screeshot and fetch the data from data base by sending a GET request by clicking on the GET button on the right upper corner.

You can filter the data using the filter button on the right upper corner. Filtering parameters are given below.
  
    * Start Date
    * End Date
    * Metrics Type (e.g. Tmin)
    * Location (e.g. UK)
    
 ![image](https://user-images.githubusercontent.com/14863485/70659334-ed8eac80-1c85-11ea-83c0-86116f3f1ce1.png)
 
 ## Note:
  You can add more Metrics and Locations following the below APIs.
   * http://127.0.0.1:8000/metric
   * http://127.0.0.1:8000/location
 
 
  
  
