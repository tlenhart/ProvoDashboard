# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('pets_rescued_at_shelter', models.IntegerField(default=0, verbose_name='Pets rescued at shelters')),
                ('calls_911', models.IntegerField(default=0, verbose_name='Number of 911 calls')),
                ('response_time_911_calls', models.IntegerField(default=0, verbose_name='Response time for 911 calls in seconds.')),
                ('noise_complaints', models.IntegerField(default=0, verbose_name='Number of noise complaints in a month.')),
                ('code_violations', models.IntegerField(default=0, verbose_name='Number of code violations in a month.')),
                ('month', models.IntegerField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')])),
                ('year', models.IntegerField(choices=[(2014, 2014), (2015, 2015)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Economic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('active_business_licenses', models.IntegerField(default=0, verbose_name='Active number of business licenses.')),
                ('building_permits_given', models.IntegerField(default=0, verbose_name='Number of building permits distributed.')),
                ('unemployment_rate', models.DecimalField(decimal_places=5, default=0.0, verbose_name='Unemployment rate as a percentage.', max_digits=5)),
                ('houses_sold', models.IntegerField(default=0, verbose_name='Number of houses sold.')),
                ('month', models.IntegerField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')])),
                ('year', models.IntegerField(choices=[(2014, 2014), (2015, 2015)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('waste_collected', models.IntegerField(default=0, verbose_name='Number of truckloads of waste collected.')),
                ('recyclables_collected', models.IntegerField(default=0, verbose_name='Number of truckloads of recyclables collected.')),
                ('level_reserve_water_tanks', models.DecimalField(decimal_places=5, default=0.0, verbose_name='Level of reserve water tanks as a percentage of capacity.', max_digits=5)),
                ('gallons_water_treated', models.DecimalField(decimal_places=2, default=0.0, verbose_name='Gallons of water treated.', max_digits=14)),
                ('home_inspections', models.IntegerField(default=0, verbose_name='Number of home inspections.')),
                ('business_inspections', models.IntegerField(default=0, verbose_name='Number of business inspections.')),
                ('month', models.IntegerField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')])),
                ('year', models.IntegerField(choices=[(2014, 2014), (2015, 2015)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecreationCultural',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('major_attractions_attended', models.IntegerField(default=0, verbose_name='Number of attendees at major attractions.')),
                ('community_program_involvement', models.IntegerField(default=0, verbose_name='Number of patrons utilizing community programs.')),
                ('recreation_center_patrons', models.IntegerField(default=0, verbose_name='Number of patrons utilizing the recreation center.')),
                ('golf_course_attendees', models.IntegerField(default=0, verbose_name='Number of attendees at the golf course.')),
                ('ice_arena_participants', models.IntegerField(default=0, verbose_name='Participants at the ice arena.')),
                ('month', models.IntegerField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')])),
                ('year', models.IntegerField(choices=[(2014, 2014), (2015, 2015)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Safety',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nonviolent_crimes_reported', models.IntegerField(default=0, verbose_name='Number of nonviolent crimes reported.')),
                ('violent_crimes_reported', models.IntegerField(default=0, verbose_name='Number of violent crimes reported.')),
                ('police_response_time', models.DecimalField(decimal_places=2, default=0.0, verbose_name='Police response time (high priority) in ...', max_digits=10)),
                ('fires_responded', models.IntegerField(default=0, verbose_name='Number of fires responded to.')),
                ('fire_response_time', models.DecimalField(decimal_places=2, default=0.0, verbose_name='Fire department response time in ...', max_digits=10)),
                ('month', models.IntegerField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')])),
                ('year', models.IntegerField(choices=[(2014, 2014), (2015, 2015)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('transportation_injuries', models.IntegerField(default=0, verbose_name='Transportation injuries.')),
                ('ontime_percent', models.DecimalField(decimal_places=5, default=0.0, verbose_name='Percentage of services on time.', max_digits=5)),
                ('auto_accidents', models.IntegerField(default=0, verbose_name='Number of auto accidents.')),
                ('public_ridership', models.DecimalField(decimal_places=3, default=0.0, verbose_name='Ridership of public transportation in thousands.', max_digits=7)),
                ('potholes_filed_YTD', models.IntegerField(default=0, verbose_name='Potholes filled YTD.')),
                ('month', models.IntegerField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')])),
                ('year', models.IntegerField(choices=[(2014, 2014), (2015, 2015)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
