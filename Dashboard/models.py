from django.db import models

##
#   Not sure if I have set this up properly (the models)
#   Might (or will) need to change so that the databases are set up properly.
##

# Create your models here.
class Community(models.Model):
    pets_rescued_at_shelter = models.IntegerField(default=0)
    calls_911 = models.IntegerField(default=0)
    response_time_911_calls = models.IntegerField(default=0) # might want to change to models.TimeField
    noise_complaints = models.IntegerField(default=0)
    code_violations = models.IntegerField(default=0)

class RecreationCultural(models.Model):
    major_attractions_attended = models.IntegerField(default=0) # Number of attendees
    community_program_involvement = models.IntegerField(default=0) # Number of patrons
    recreation_center_patrons = models.IntegerField(default=0)
    golf_course_attendees = models.IntegerField(default=0)
    ice_arena_participants = models.IntegerField(default=0)

class Economic(models.Model):
    active_business_licenses = models.IntegerField(default=0)
    building_permits_given = models.IntegerField(default=0)
    unemployment_rate = models.DecimalField(default=0.0) # Need to decide how this is going to be stored. 0.33 or 33 for 33%.
    houses_sold = models.IntegerField(default=0)

class Environment(models.Model):
    waste_collected = models.IntegerField(default=0) # Number of Truckloads
    recyclables_collected = models.IntegerField(default=0) # Number of Truckloads
    level_reserve_water_tanks = models.DecimalField(default=0.0) # % of capacity. Need to decide how this is going to be stored. 0.33 or 33 for 33%.
    gallons_water_treated = models.DecimalField(default=0.0) # Could maybe change to an integer.
    home_inspections = models.IntegerField(default=0)
    business_inspections = models.IntegerField(default=0)

class Safety(models.Model):
    nonviolent_crimes_reported = models.IntegerField(default=0)
    violent_crimes_reported = models.IntegerField(default=0)
    police_response_time = models.DecimalField(default=0.0) # Might need to change to police_response_time_high_priority
    fires_responded = models.IntegerField(default=0)
    fire_response_time = models.DecimalField(default=0.0)

class Transportation(models.Model):
    transportation_injuries = models.IntegerField(default=0)
    ontime_percent = models.DecimalField(default=0.0)
    auto_accidents = models.IntegerField(default=0)
    public_ridership = models.DecimalField(default=0.0) # In thousands. Multiply by 1000 if necessary. Storing 19.1 would equal 19,100.
    potholes_filed_YTD = models.IntegerField(default=0)


