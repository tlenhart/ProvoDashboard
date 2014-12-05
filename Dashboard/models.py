from django.db import models
from django.contrib.auth.models import User

##
#   Not sure if I have set this up properly (the models)
#   Might (or will) need to change so that the databases are set up properly.
#   The fields in each class are columns in the database. I think I have this wrong.
#
#   Anything that is a DecimalField requires a max_digits and a decimal_places.
#   These may need to be adjusted based on how we want the numbers to be saved/stored.
#
#   No keys currently exist in the tables that point to other tables...
#   For example, community = models.ForeignKey(Community)
#
##

# Create your models here.

YEARS = (
    (2014, 2014),
    (2015, 2015)
)

MONTHS = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December")
)

DEPARTMENT = (
    ("Community_Neighborhood_Livability", "Community Neighborhood Livability"),
    ("Cultural_and_Recreation","Cultural and Recreation")
)

class DashboardData(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    category = models.CharField(choices=DEPARTMENT, max_length=100)
    value = models.DecimalField(decimal_places=2, max_digits=11)
    month = models.IntegerField(choices=MONTHS)
    year = models.IntegerField(choices=YEARS)
    def __str__(self):
        return "Database Data."

class Community(models.Model):
    pets_rescued_at_shelter = models.IntegerField('Pets rescued at shelters', default=0)
    calls_911 = models.IntegerField('Number of 911 calls', default=0)
    response_time_911_calls = models.IntegerField('Response time for 911 calls in seconds.', default=0) # might want to change to models.TimeField
    noise_complaints = models.IntegerField('Number of noise complaints in a month.', default=0)
    code_violations = models.IntegerField('Number of code violations in a month.', default=0)
    month = models.IntegerField(choices=MONTHS)
    year = models.IntegerField(choices=YEARS)

    def __str__(self):
        return "Database table for Community, Neighborhood, and Livability."

class RecreationCultural(models.Model):
    major_attractions_attended = models.IntegerField('Number of attendees at major attractions.',default=0) # Number of attendees
    community_program_involvement = models.IntegerField('Number of patrons utilizing community programs.',default=0) # Number of patrons
    recreation_center_patrons = models.IntegerField('Number of patrons utilizing the recreation center.',default=0)
    golf_course_attendees = models.IntegerField('Number of attendees at the golf course.',default=0)
    ice_arena_participants = models.IntegerField('Participants at the ice arena.',default=0)
    month = models.IntegerField(choices=MONTHS)
    year = models.IntegerField(choices=YEARS)

    def __str__(self):
        return "Database table for Recreation and Cultural."

class Economic(models.Model):
    active_business_licenses = models.IntegerField('Active number of business licenses.',default=0)
    building_permits_given = models.IntegerField('Number of building permits distributed.',default=0)
    unemployment_rate = models.DecimalField('Unemployment rate as a percentage.',default=0.0,max_digits=5,decimal_places=5) # Need to decide how this is going to be stored. 0.33 or 33 for 33%.
    houses_sold = models.IntegerField('Number of houses sold.', default=0)
    month = models.IntegerField(choices=MONTHS)
    year = models.IntegerField(choices=YEARS)

    def __str__(self):
        return "Database table for Economic Health."

class Environment(models.Model):
    waste_collected = models.IntegerField('Number of truckloads of waste collected.',default=0) # Number of Truckloads
    recyclables_collected = models.IntegerField('Number of truckloads of recyclables collected.',default=0) # Number of Truckloads
    level_reserve_water_tanks = models.DecimalField('Level of reserve water tanks as a percentage of capacity.',default=0.0,max_digits=5,decimal_places=5) # % of capacity. Need to decide how this is going to be stored. 0.33 or 33 for 33%.
    gallons_water_treated = models.DecimalField('Gallons of water treated.',default=0.0,max_digits=14,decimal_places=2) # Could maybe change to an integer. max_digits=14 and decimal_places=2 allows up to 999,999,999,999.99 gallons of water to be stored. (Unless I'm mistaken...)
    home_inspections = models.IntegerField('Number of home inspections.',default=0)
    business_inspections = models.IntegerField('Number of business inspections.',default=0)
    month = models.IntegerField(choices=MONTHS)
    year = models.IntegerField(choices=YEARS)

    def __str__(self):
        return "Database table for Environmental Health."

class Safety(models.Model):
    nonviolent_crimes_reported = models.IntegerField('Number of nonviolent crimes reported.',default=0)
    violent_crimes_reported = models.IntegerField('Number of violent crimes reported.',default=0)
    police_response_time = models.DecimalField('Police response time (high priority) in ...',default=0.0,max_digits=10,decimal_places=2) # Might need to change to police_response_time_high_priority
    fires_responded = models.IntegerField('Number of fires responded to.',default=0)
    fire_response_time = models.DecimalField('Fire department response time in ...',default=0.0,max_digits=10,decimal_places=2)
    month = models.IntegerField(choices=MONTHS)
    year = models.IntegerField(choices=YEARS)

    def __str__(self):
        return "Database table for Public Safety."

class Transportation(models.Model):
    transportation_injuries = models.IntegerField('Transportation injuries.', default=0)
    ontime_percent = models.DecimalField('Percentage of services on time.', default=0.0,max_digits=5,decimal_places=5)
    auto_accidents = models.IntegerField('Number of auto accidents.', default=0)
    public_ridership = models.DecimalField('Ridership of public transportation in thousands.',default=0.0,max_digits=7,decimal_places=3) # In thousands. Multiply by 1000 if necessary. Storing 19.1 would equal 19,100.
    potholes_filed_YTD = models.IntegerField('Potholes filled YTD.', default=0)
    month = models.IntegerField(choices=MONTHS)
    year = models.IntegerField(choices=YEARS)


    def __str__(self):
        return "Database table for Transportation."





