# Ambuj_Assignment

#  1st Part
## Requirements

* Python (3.5 or above)
* Django (2.2 or above)

### Project setup:
* Open your command line(press Window + r and run after typing cmd) open your working directory run command using `git`...
     $git clone https://github.com/ambujap94/Ambuj_Assignment.git
     
* change the directory to Ambuj_Assignment by  `cd Ambuj_Assignment`

* Install virtualenv in your system using the command `pip install virtualenv`.

* Type the command `virtualenv venv` to create a virtual environment by the name of venv.

* Install all the requirements and dependencies using the requirement.txt file by `pip install -r requirements.txt`


### Testing Browsable API

run the server using command `python manage.py runserver` and open the link
  http://127.0.0.1:8000/weatherdata
  
  ![image](https://user-images.githubusercontent.com/14863485/70658915-fc289400-1c84-11ea-8849-3d2dd3cbf7c8.png)

Now you can post data from the HTML form in the above screeshot and see the data by clicking on the GET button on the right upper corner.

You can filter the data by clicking on the Filter button on the right upper corner.
  * filter by:
    * Start Date
    * End Date
    * Metrics Type (e.g. Tmin)
    * Location (e.g. UK)
    
 ![image](https://user-images.githubusercontent.com/14863485/70659334-ed8eac80-1c85-11ea-83c0-86116f3f1ce1.png)
 
 ## Note:
  You can add more Metrics and Locations following the below APIs.
   * http://127.0.0.1:8000/metric
   * http://127.0.0.1:8000/location
 
 ### Unit Test:
  * Tests are written for GET and POT success and Post failure cases and can be checked by running a command 
  `python manage.py test`. Test cases were passed when cheked.
  
 # 2nd Part
  ## Management Command
  
  
