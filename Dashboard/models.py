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
    ("Community", "Community Neighborhood Livability"),
    ("Culture", "Cultural and Recreation"),
    ("Economic", "Economic Health"),
    ("Environment", "Environmental Health"),
    ("Safety", "Community Safety"),
    ("Transportation", "Transportation")
)

COMMUNITY_CATEGORIES = (
    ("Pets_Rescued", "Pets Rescued at Shelter"),
    ("911_Calls", "911 Calls"),
    ("911_Response", "911 Phone Response Time (seconds)"),
    ("Noise_Complaints", "Noise Complaints"),
    ("Code_Violations", "Code Violations")

)

RECREATION_CATEGORIES = (
    ("Major_Attractions", "Major Attractions Attended (# of attendees"),
    ("Community_Involvement", "Community Program Involvement (# of patrons"),
    ("Rec_Center_Patrons", "Recreation Center Patrons"),
    ("Golf_Course_Patrons", "Golf Course Patrons"),
    ("Ice_Arena_Participants", "Ice Arena Participants")
)

ECONOMIC_CATEGORIES = (
    ("Active_Licenses", "Active Number of Business Licenses"),
    ("Building_Permits", "Building Permits Issued"),
    ("Unemployment_Rate", "Unemployment Rate"),
    ("Houses_Sold", "Houses Sold")
)

ENVIRONMENT_CATEGORIES = (
    ("Waste_Collected", "Waste Collected (Truck Loads)"),
    ("Recyclables_Collected", "Recyclables Collected (Truck Loads"),
    ("Water_Level", "Level of Reserve Water Tanks (% of capacity)"),
    ("Water_Treated", "Gallons of Water Treated"),
    ("Home_Inspections", "Home Inspections"),
    ("Business_Inspections", "Business Inspections")
)

SAFETY_CATEGORIES = (
    ("Nonviolent_Crimes", "Nonviolent Crimes Reported"),
    ("Violent_Crimes", "Violent Crimes Reported"),
    ("Police_Response_Time", "Police Response Time (High Priority)"),
    ("Fires_Responded", "Fires Responded"),
    ("Fire_Response_Time", "Fire_Response_Time")
)

TRANSPORTATION_CATEGORIES = (
    ("Transportation_Injuries", "Transportation Injuries"),
    ("On_time_Rate", "Percentage On Time"),
    ("Auto_Accidents", "Auto Accidents"),
    ("Ridership", "Public Ridership (In thousands)"),
    ("Pot_holes_Filled", "Pot Holes Filled (YTD)")
)


class Community(models.Model):
    # pets_rescued_at_shelter = models.IntegerField('Pets rescued at shelters', default=0)
    # calls_911 = models.IntegerField('Number of 911 calls', default=0)
    # might want to change to models.TimeField #
    # response_time_911_calls = models.IntegerField('Response time for 911 calls in seconds.', default=0)
    # noise_complaints = models.IntegerField('Number of noise complaints in a month.', default=0)
    # code_violations = models.IntegerField('Number of code violations in a month.', default=0)
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    category = models.CharField(choices=COMMUNITY_CATEGORIES, max_length=100)
    value = models.DecimalField(decimal_places=2, max_digits=11)
    month = models.CharField(choices=MONTHS, max_length=20)
    year = models.IntegerField(choices=YEARS)

    def __str__(self):
        return "Database table for Community, Neighborhood, and Livability."


class RecreationCultural(models.Model):
    # Number of attendees
    # major_attractions_attended = models.IntegerField('Number of attendees at major attractions.',default=0)
    # Number of patrons
    # community_program_involvement = models.IntegerField('Number of patrons utilizing community programs.',default=0)
    # recreation_center_patrons = models.IntegerField('Number of patrons utilizing the recreation center.',default=0)
    # golf_course_attendees = models.IntegerField('Number of attendees at the golf course.',default=0)
    # ice_arena_participants = models.IntegerField('Participants at the ice arena.',default=0)
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    category = models.CharField(choices=RECREATION_CATEGORIES, max_length=100)
    value = models.DecimalField(decimal_places=2, max_digits=11)
    month = models.CharField(choices=MONTHS, max_length=20)
    year = models.IntegerField(choices=YEARS)

    def __str__(self):
        return "Database table for Recreation and Cultural."


class Economic(models.Model):
    # active_business_licenses = models.IntegerField('Active number of business licenses.',default=0)
    # building_permits_given = models.IntegerField('Number of building permits distributed.',default=0)
    # Need to decide how this is going to be stored. 0.33 or 33 for 33%.
    # unemployment_rate = models.DecimalField('Unemployment rate as a percentage.',
    #                                     default=0.0,max_digits=5,decimal_places=5)
    # houses_sold = models.IntegerField('Number of houses sold.', default=0)
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    category = models.CharField(choices=ECONOMIC_CATEGORIES, max_length=100)
    value = models.DecimalField(decimal_places=2, max_digits=11)
    month = models.CharField(choices=MONTHS, max_length=20)
    year = models.IntegerField(choices=YEARS)

    def __str__(self):
        return "Database table for Economic Health."


class Environment(models.Model):
    # waste_collected = models.IntegerField('Number of truckloads of waste collected.',default=0) # Number of Truckloads
    # Number of Truckloads
    # recyclables_collected = models.IntegerField('Number of truckloads of recyclables collected.',default=0)
    # % of capacity. Need to decide how this is going to be stored. 0.33 or 33 for 33%.
    # level_reserve_water_tanks = models.DecimalField('Level of reserve water tanks as a percentage of capacity.'
    #                                                                   ,default=0.0,max_digits=5,decimal_places=5)
    # Could maybe change to an integer. max_digits=14 and decimal_places=2 allows up to 999,999,999,999.99 gallons
    #  of water to be stored. (Unless I'm mistaken...)
    # gallons_water_treated = models.DecimalField('Gallons of water treated',default=0.0,max_digits=14,decimal_places=2)
    # home_inspections = models.IntegerField('Number of home inspections.',default=0)
    # business_inspections = models.IntegerField('Number of business inspections.',default=0)
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    category = models.CharField(choices=ENVIRONMENT_CATEGORIES, max_length=100)
    value = models.DecimalField(decimal_places=2, max_digits=11)
    month = models.CharField(choices=MONTHS, max_length=20)
    year = models.IntegerField(choices=YEARS)

    def __str__(self):
        return "Database table for Environmental Health."


class Safety(models.Model):
    # nonviolent_crimes_reported = models.IntegerField('Number of nonviolent crimes reported.',default=0)
    # violent_crimes_reported = models.IntegerField('Number of violent crimes reported.',default=0)
    # Might need to change to police_response_time_high_priority
    # police_response_time = models.DecimalField('Police response time',default=0.0,max_digits=10,decimal_places=2)
    # fires_responded = models.IntegerField('Number of fires responded to.',default=0)
    # fire_response_time = models.DecimalField('Fire department response time,default=0.0,max_digits=9,decimal_places=2)
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    category = models.CharField(choices=SAFETY_CATEGORIES, max_length=100)
    value = models.DecimalField(decimal_places=2, max_digits=11)
    month = models.CharField(choices=MONTHS, max_length=20)
    year = models.IntegerField(choices=YEARS)

    def __str__(self):
        return "Database table for Public Safety."


class Transportation(models.Model):
    # transportation_injuries = models.IntegerField('Transportation injuries.', default=0)
    # ontime_percent = models.DecimalField('Percentage of services on time.', default=0.0,max_digits=5,decimal_places=5)
    # auto_accidents = models.IntegerField('Number of auto accidents.', default=0)
    # In thousands. Multiply by 1000 if necessary. Storing 19.1 would equal 19,100.
    # public_ridership = models.DecimalField('Ridership',default=0.0,max_digits=7,decimal_places=3)
    # potholes_filed_YTD = models.IntegerField('Potholes filled YTD.', default=0)
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    category = models.CharField(choices=TRANSPORTATION_CATEGORIES, max_length=100)
    value = models.DecimalField(decimal_places=2, max_digits=11)
    month = models.CharField(choices=MONTHS, max_length=20)
    year = models.IntegerField(choices=YEARS)

    def __str__(self):
        return "Database table for Transportation."
