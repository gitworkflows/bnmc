# Generated by Django 2.0.7 on 2018-07-31 21:45

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'STAFF',
                'verbose_name_plural': 'STAFFS',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='District Name')),
            ],
            options={
                'verbose_name': 'DISTRICT',
                'verbose_name_plural': 'DISTRICT',
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Division Name')),
            ],
            options={
                'verbose_name': 'DIVISION',
                'verbose_name_plural': 'DIVISION',
            },
        ),
        migrations.CreateModel(
            name='EducationQualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_of_education', models.CharField(blank=True, max_length=120, null=True, verbose_name='Level Of Education')),
                ('education_type', models.CharField(choices=[('1', 'Science'), ('2', 'Comerce'), ('3', 'Arts'), ('4', 'Enginnering'), ('5', 'Nursing'), ('6', 'Doctorate'), ('7', 'Professional')], max_length=120, verbose_name='Education Type')),
                ('board', models.CharField(blank=True, max_length=120, null=True, verbose_name='University/Board')),
                ('roll', models.CharField(blank=True, max_length=120, null=True, verbose_name='Roll')),
                ('cgpa', models.CharField(blank=True, max_length=120, null=True, verbose_name='CGPA')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Ýear')),
                ('duration', models.CharField(blank=True, choices=[('1', '1 year'), ('2', '2 years'), ('3', '3 years'), ('4', '4years')], max_length=120, null=True, verbose_name='Duration')),
                ('country', models.CharField(blank=True, choices=[('1', 'Bangladesh'), ('2', 'Pakistan'), ('3', 'India'), ('4', 'Nepal'), ('5', 'Sri Lanka'), ('6', 'Bhutan'), ('7', 'Maldives'), ('8', 'Afghanistan')], max_length=120, null=True, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=120, verbose_name='Exam Name')),
                ('exam_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Exam Code')),
                ('pass_mark', models.IntegerField(blank=True, null=True, verbose_name='Pass Mark')),
            ],
            options={
                'verbose_name': 'EXAM',
                'verbose_name_plural': 'EXAMS',
            },
        ),
        migrations.CreateModel(
            name='ExamCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=200, verbose_name='Center Name')),
                ('institution_code', models.CharField(max_length=100, verbose_name='Center Code')),
                ('village', models.CharField(max_length=200)),
                ('post_office', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InstituteCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=120, verbose_name='Institution Catagory Name')),
            ],
            options={
                'verbose_name': 'INSTITUTE CATEGORY',
                'verbose_name_plural': 'INSTITUTE CATEGORIES',
            },
        ),
        migrations.CreateModel(
            name='InstituteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_type', models.CharField(max_length=120, verbose_name='Institution Type')),
            ],
            options={
                'verbose_name': 'INSTITUTE TYPE',
                'verbose_name_plural': 'INSTITUTE TYPES',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=200, verbose_name='Institution Name')),
                ('institution_code', models.CharField(max_length=100, verbose_name='Institution Code')),
                ('village', models.CharField(max_length=200)),
                ('post_office', models.CharField(blank=True, max_length=100)),
                ('is_exam_center', models.BooleanField(verbose_name='Is Exam Center')),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.InstituteCatagory', verbose_name='Institution Catagory ')),
                ('district', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='division', chained_model_field='division', on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.District')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Division')),
                ('exam_ins', models.ManyToManyField(blank=True, to='bnmc_project.Exam', verbose_name='Exam')),
            ],
            options={
                'verbose_name': 'INSTITUTION ',
                'verbose_name_plural': 'INSTITUTIONS',
            },
        ),
        migrations.CreateModel(
            name='license_receive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300, verbose_name='Full name (Bangla)')),
                ('last_name', models.CharField(max_length=300, verbose_name='Full name (English)')),
                ('date_of_birth', models.DateField()),
                ('national_ID_No', models.CharField(blank=True, max_length=128)),
                ('village', models.CharField(max_length=300)),
                ('post_office', models.CharField(max_length=300)),
                ('postal_code', models.CharField(blank=True, max_length=300)),
                ('license_start_date', models.DateField(blank=True, max_length=120, null=True)),
                ('license_end_date', models.DateField(blank=True, null=True)),
                ('district', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='division', chained_model_field='division', null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.District')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Division')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='license_registrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='media/', verbose_name='Upload photo')),
                ('image_sec', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Upload photo')),
                ('date_of_passing_on', models.DateField()),
                ('registration_no', models.IntegerField(blank=True, default=0, null=True)),
                ('first_name', models.CharField(max_length=300, verbose_name='Full name (Bangla)')),
                ('last_name', models.CharField(max_length=300, verbose_name='Full name (English)')),
                ('fathers_name', models.CharField(max_length=300)),
                ('mothers_name', models.CharField(max_length=300)),
                ('sex', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Others')], max_length=12)),
                ('religions', models.CharField(choices=[('1', 'Islam'), ('2', 'Hindu'), ('3', 'Buddhist'), ('4', 'Christian'), ('5', 'Others')], max_length=120)),
                ('students_mobile_no', models.CharField(max_length=200)),
                ('village', models.CharField(max_length=300)),
                ('post_office', models.CharField(max_length=300)),
                ('postal_code', models.CharField(blank=True, max_length=300)),
                ('signature_first', models.ImageField(blank=True, upload_to='media/', verbose_name='Upload photo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('signature_sec', models.ImageField(blank=True, upload_to='media/', verbose_name='up photo')),
                ('approved', models.BooleanField(default=False)),
                ('image_field', models.CharField(blank=True, max_length=200, null=True)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='center', to='bnmc_project.ExamCenter')),
                ('district', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='division', chained_model_field='division', null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.District')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Division')),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='institution', to='bnmc_project.Institution')),
            ],
            options={
                'verbose_name': 'LICENSE REGISTRATION',
                'verbose_name_plural': 'LICENSE REGISTRATIONS',
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationality_name', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'NATIONALITY',
                'verbose_name_plural': 'NATIONALITYS',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_no', models.PositiveIntegerField(blank=True, null=True)),
                ('permission_name', models.CharField(blank=True, max_length=120)),
                ('display_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'verbose_name': 'PERMISSION',
                'verbose_name_plural': 'PERMISSIONS',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Program Name')),
                ('code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Program Code')),
                ('minimum_grade', models.FloatField(verbose_name='Minimum Grade')),
                ('program_fee', models.CharField(blank=True, max_length=10, null=True, verbose_name='Program Fee')),
            ],
            options={
                'verbose_name': 'PROGRAM ',
                'verbose_name_plural': 'PROGRAMS',
            },
        ),
        migrations.CreateModel(
            name='ProgramCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Program Catagory Name')),
            ],
            options={
                'verbose_name': 'PROGRAM CATEGORY',
                'verbose_name_plural': 'PROGRAM CATEGORIES',
            },
        ),
        migrations.CreateModel(
            name='ProgramDuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DecimalField(decimal_places=9, max_digits=10, verbose_name='Program Duration')),
            ],
            options={
                'verbose_name': 'PROGRAM DURATION',
                'verbose_name_plural': 'PROGRAM DURATIONS',
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum_qualification', models.CharField(max_length=100, verbose_name='Minimum Qualification')),
            ],
            options={
                'verbose_name': 'QUALIFICATIION',
                'verbose_name_plural': 'QUALIFICATIIONS',
            },
        ),
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota_name', models.CharField(max_length=120, null=True)),
            ],
            options={
                'verbose_name': 'QUOTA',
                'verbose_name_plural': 'QUOTAS',
            },
        ),
        migrations.CreateModel(
            name='Relation_to_guardians',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'RELATION TO GUARDIANS',
                'verbose_name_plural': 'RELATION TO GUARDIANS',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=120)),
                ('is_active', models.BooleanField(default=False)),
                ('session_start_date', models.DateField(null=True)),
                ('session_end_date', models.DateField(null=True)),
            ],
            options={
                'verbose_name': 'SESSION',
                'verbose_name_plural': 'SESSIONS',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='media/', verbose_name='Upload photo')),
                ('registration_no', models.CharField(blank=True, default=0, max_length=120, null=True)),
                ('has_student_id', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('fathers_name', models.CharField(max_length=300)),
                ('mothers_name', models.CharField(max_length=300)),
                ('sex', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Others')], max_length=12)),
                ('date_of_birth', models.DateField()),
                ('national_ID_No', models.CharField(blank=True, max_length=128)),
                ('passport_no', models.CharField(blank=True, max_length=128)),
                ('guardians_name', models.CharField(blank=True, max_length=300)),
                ('religions', models.CharField(choices=[('1', 'Islam'), ('2', 'Hindu'), ('3', 'Buddhist'), ('4', 'Christian'), ('5', 'Others')], max_length=120)),
                ('marital_status', models.CharField(choices=[('1', 'Single'), ('2', 'Married'), ('3', 'Widow'), ('4', 'Divorce'), ('5', 'Separated')], max_length=120)),
                ('email_address', models.EmailField(blank=True, max_length=128)),
                ('students_mobile_no', models.CharField(blank=True, max_length=200)),
                ('union', models.CharField(blank=True, max_length=300)),
                ('village', models.CharField(blank=True, max_length=300)),
                ('post_office', models.CharField(blank=True, max_length=300)),
                ('postal_code', models.CharField(blank=True, max_length=300)),
                ('village_snd', models.CharField(max_length=300, verbose_name='Village')),
                ('post_office_snd', models.CharField(max_length=300, verbose_name='Post office')),
                ('postal_code_snd', models.CharField(blank=True, max_length=300, verbose_name='Postal code')),
                ('district', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='division', chained_model_field='division', null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.District')),
                ('district_snd', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='division', chained_model_field='division', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dIsItRiCt', to='bnmc_project.District', verbose_name='District')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Division')),
                ('division_snd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dIviSiOn', to='bnmc_project.Division', verbose_name='Division')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Institution')),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Nationality')),
                ('quota', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Quota')),
                ('relation_to_guardians', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Relation_to_guardians')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='media/', verbose_name='Upload photo')),
                ('registration_no', models.CharField(blank=True, default=0, max_length=120, null=True)),
                ('first_name', models.CharField(max_length=300, verbose_name='Full name (Bangla)')),
                ('last_name', models.CharField(max_length=300, verbose_name='Full name (English)')),
                ('fathers_name', models.CharField(max_length=300)),
                ('mothers_name', models.CharField(max_length=300)),
                ('guardians_name', models.CharField(blank=True, max_length=300)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Others')], max_length=12)),
                ('religions', models.CharField(choices=[('1', 'Islam'), ('2', 'Hindu'), ('3', 'Buddhist'), ('4', 'Christian'), ('5', 'Others')], max_length=120)),
                ('marital_status', models.CharField(choices=[('1', 'Single'), ('2', 'Married'), ('3', 'Widow'), ('4', 'Divorce'), ('5', 'Separated')], max_length=120)),
                ('national_ID_No', models.CharField(blank=True, max_length=128)),
                ('passport_no', models.CharField(blank=True, max_length=128)),
                ('students_mobile_no', models.CharField(max_length=200)),
                ('email_address', models.EmailField(blank=True, max_length=128)),
                ('village', models.CharField(max_length=300)),
                ('post_office', models.CharField(max_length=300)),
                ('postal_code', models.CharField(blank=True, max_length=300)),
                ('same_address', models.BooleanField()),
                ('village_snd', models.CharField(max_length=300, verbose_name='Village')),
                ('post_office_snd', models.CharField(max_length=300, verbose_name='Post office')),
                ('postal_code_snd', models.CharField(blank=True, max_length=300, verbose_name='Postal code')),
                ('date_of_registration', models.DateField(blank=True, max_length=120, null=True)),
                ('program_starting_date', models.DateField(blank=True, null=True)),
                ('payment_method', models.CharField(choices=[('1', 'Bank Draft'), ('2', 'Cash'), ('3', 'Cheque')], max_length=120)),
                ('registration_fees', models.CharField(blank=True, max_length=120)),
                ('bank_draft_no', models.CharField(blank=True, max_length=300, null=True, verbose_name='Bank Draft No. ')),
                ('bank_draft_date', models.DateField(blank=True, max_length=300, null=True, verbose_name='Bank Draft Date ')),
                ('program_completion_date', models.DateField(blank=True, null=True)),
                ('view_type', models.IntegerField(blank=True, default=1)),
                ('re_id', models.CharField(blank=True, max_length=120, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('migration', models.BooleanField(default=False, verbose_name='migrateable')),
                ('migration_approval_bnmc', models.BooleanField(default=False)),
                ('migration_date', models.DateField(blank=True, null=True)),
                ('student_id', models.CharField(blank=True, max_length=120)),
                ('district', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='division', chained_model_field='division', null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.District')),
                ('district_snd', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='division', chained_model_field='division', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='District', to='bnmc_project.District', verbose_name='District')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Division')),
                ('division_snd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Division', to='bnmc_project.Division', verbose_name='Division')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Institution')),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Nationality')),
                ('new_institute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='new_institution', to='bnmc_project.Institution')),
                ('old_institute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='old_intitution', to='bnmc_project.Institution')),
                ('program_title', models.ForeignKey(max_length=120, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Program')),
                ('quota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Quota')),
                ('relation_to_guardians', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Relation_to_guardians')),
                ('session', models.ForeignKey(max_length=120, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Session')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Permission')),
                ('students', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Student')),
            ],
            options={
                'verbose_name': 'STUDENT REGISTRATIONS',
                'verbose_name_plural': 'STUDENT REGISTRATIONS',
            },
        ),
        migrations.CreateModel(
            name='Thana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Police Station Name')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.District', verbose_name='District Name')),
            ],
            options={
                'verbose_name': 'THANA',
                'verbose_name_plural': 'THANA',
            },
        ),
        migrations.AddField(
            model_name='student_registration',
            name='thana',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='district', chained_model_field='district', null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Thana'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='thana_snd',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='district', chained_model_field='district', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thana', to='bnmc_project.Thana', verbose_name='Thana'),
        ),
        migrations.AddField(
            model_name='student',
            name='thana',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='district', chained_model_field='district', null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Thana'),
        ),
        migrations.AddField(
            model_name='student',
            name='thana_snd',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='district', chained_model_field='district', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tHaNa', to='bnmc_project.Thana', verbose_name='Thana'),
        ),
        migrations.AddField(
            model_name='program',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.ProgramCatagory', verbose_name='Program Catagory '),
        ),
        migrations.AddField(
            model_name='program',
            name='duration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.ProgramDuration', verbose_name='Program Duration'),
        ),
        migrations.AddField(
            model_name='program',
            name='minimum_qualification',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Qualification', verbose_name='Minimum Qualification'),
        ),
        migrations.AddField(
            model_name='program',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Session'),
        ),
        migrations.AddField(
            model_name='license_registrations',
            name='nationality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Nationality'),
        ),
        migrations.AddField(
            model_name='license_registrations',
            name='program_title',
            field=models.ForeignKey(blank=True, max_length=120, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Exam'),
        ),
        migrations.AddField(
            model_name='license_registrations',
            name='session',
            field=models.ForeignKey(max_length=120, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Session'),
        ),
        migrations.AddField(
            model_name='license_registrations',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Permission'),
        ),
        migrations.AddField(
            model_name='license_registrations',
            name='students',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Student'),
        ),
        migrations.AddField(
            model_name='license_registrations',
            name='thana',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='district', chained_model_field='district', null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Thana'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='nationality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Nationality'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='program_title',
            field=models.ForeignKey(max_length=120, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Program'),
        ),
        migrations.AddField(
            model_name='license_receive',
            name='thana',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='district', chained_model_field='district', null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Thana'),
        ),
        migrations.AddField(
            model_name='institution',
            name='program_ins',
            field=models.ManyToManyField(blank=True, to='bnmc_project.Program', verbose_name='Program'),
        ),
        migrations.AddField(
            model_name='institution',
            name='thana',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='district', chained_model_field='district', on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Thana'),
        ),
        migrations.AddField(
            model_name='institution',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.InstituteType', verbose_name='Institution Type '),
        ),
        migrations.AddField(
            model_name='examcenter',
            name='catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.InstituteCatagory', verbose_name='Center Catagory '),
        ),
        migrations.AddField(
            model_name='examcenter',
            name='district',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='division', chained_model_field='division', on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.District'),
        ),
        migrations.AddField(
            model_name='examcenter',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Division'),
        ),
        migrations.AddField(
            model_name='examcenter',
            name='thana',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='district', chained_model_field='district', on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Thana'),
        ),
        migrations.AddField(
            model_name='examcenter',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.InstituteType', verbose_name='Center Type '),
        ),
        migrations.AddField(
            model_name='educationqualification',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Student_Registration'),
        ),
        migrations.AddField(
            model_name='educationqualification',
            name='students',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Student'),
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnmc_project.Division', verbose_name='Division Name'),
        ),
        migrations.AddField(
            model_name='user',
            name='show_permission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='show_permission_permissions', to='bnmc_project.Permission'),
        ),
        migrations.AddField(
            model_name='user',
            name='staff_institute',
            field=models.ManyToManyField(blank=True, related_name='head_of', to='bnmc_project.Institution'),
        ),
        migrations.AddField(
            model_name='user',
            name='staff_status',
            field=models.ManyToManyField(related_name='staff_status_permissions', to='bnmc_project.Permission'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
