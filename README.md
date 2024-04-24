## Flask-Based REST API prepared for the midterm assignment of the SE 3355 Web Programming course.
# SQLALCHEMY ORM and cloud-hosted Microsoft SQL server used

## System Structure
![system diagram 3355mterm](https://github.com/gunesgultekin/SE3355-FlaskAPI/assets/126399958/1e2bec8e-07a2-4d63-a37f-8bc528c963ea)

## Data Model
![midtermDataModel](https://github.com/gunesgultekin/SE3355-FlaskAPI/assets/126399958/f3d21cb6-a511-4ae9-a7ca-ed85348f53bc)

## ! Problems
* Azure SQL database pauses the database after a certain period of time due to the 'auto-pause' feature. Therefore, images and information may not be loaded when you first enter the site. (Deployment link provided) The database will be accessed automatically within 1 minute and the API will respond to requests.
