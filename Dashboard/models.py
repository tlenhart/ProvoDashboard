from django.db import models
from django.contrib.auth.models import User

# #
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
    (2015, 2015),
    (2016, 2016),
    (2017, 2017)
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


class SubCategories(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    sub_category = models.CharField(max_length=300, default="Please Add A Category")
    description = models.CharField(max_length=1000, null=False)
    main_category = models.CharField(max_length=300, null=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return "{0} **{1}** ".format(self.sub_category, self.main_category)


class PublicSafety(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    category = models.ForeignKey(SubCategories)
    value = models.DecimalField(decimal_places=2, max_digits=11)
    month = models.CharField(choices=MONTHS, max_length=20)
    year = models.IntegerField(choices=YEARS)

    class Meta:
        unique_together = ["category", "month", "year"]

    def __str__(self):
        return "{0} - {1}, {2}".format(self.category, self.month, self.year)


class CivicHealth(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    category = models.ForeignKey(SubCategories)
    value = models.DecimalField(decimal_places=2, max_digits=11)
    month = models.CharField(choices=MONTHS, max_length=20)
    year = models.IntegerField(choices=YEARS)

    class Meta:
        unique_together = ["category", "month", "year"]

    def __str__(self):
        return "{0} - {1}, {2}".format(self.category, self.month, self.year)


class EconomicHealth(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    category = models.ForeignKey(SubCategories)
    value = models.DecimalField(decimal_places=2, max_digits=11)
    month = models.CharField(choices=MONTHS, max_length=20)
    year = models.IntegerField(choices=YEARS)

    class Meta:
        unique_together = ["category", "month", "year"]

    def __str__(self):
        return "{0} - {1}, {2}".format(self.category, self.month, self.year)


class GovernmentPerformance(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    category = models.ForeignKey(SubCategories)
    value = models.DecimalField(decimal_places=2, max_digits=11)
    month = models.CharField(choices=MONTHS, max_length=20)
    year = models.IntegerField(choices=YEARS)

    class Meta:
        unique_together = ["category", "month", "year"]

    def __str__(self):
        return "{0} - {1}, {2}".format(self.category, self.month, self.year)


class Safety(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    category = models.ForeignKey(SubCategories)
    value = models.DecimalField(decimal_places=2, max_digits=11)
    month = models.CharField(choices=MONTHS, max_length=20)
    year = models.IntegerField(choices=YEARS)

    class Meta:
        unique_together = ["category", "month", "year"]

    def __str__(self):
        return "{0} - {1}, {2}".format(self.category, self.month, self.year)