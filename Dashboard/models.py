from django.db import models
from django.contrib.auth.models import User

# #
#   The fields in each class are columns in the database.
#
#   Anything that is a DecimalField requires a max_digits and a decimal_places.
#   These may need to be adjusted based on how we want the numbers to be saved/stored.
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

# These might need to change based on what we get working on the front-end with Angular.
GRAPHCHOICE = (
    ("chart-polar", "Polar"),
    ("chart-bar", "Bar"),
    ("chart-line", "Line"),
    ("chart-none", "None"),
    ("chart-doughnut", "Doughnut"),
    ("chart-pie", "Pie"),
    ("chart-radar", "Radar")
)

MAINCATEGORIES = (
    ("Civic Health", "Civic Health"),
    ("Economic Health", "Economic Health"),
    ("Government Performance", "Government Performance"),
    ("Public Safety", "Public Safety")
)


class SubCategories(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    sub_category = models.CharField(max_length=300, default="Please Add A Category")
    description = models.CharField(max_length=1000, null=False)
    main_category = models.CharField(max_length=300, null=False, choices=MAINCATEGORIES)
    chart_type = models.CharField(max_length=25, null=True, default="Base", choices=GRAPHCHOICE)
    visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Subcategories"

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
        verbose_name_plural = "Public Safety"

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
        verbose_name_plural = "Civic Health"

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
        verbose_name_plural = "Economic Health"

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
        verbose_name_plural = "Government Performance"

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
        verbose_name_plural = "Public Safety"

    def __str__(self):
        return "{0} - {1}, {2}".format(self.category, self.month, self.year)