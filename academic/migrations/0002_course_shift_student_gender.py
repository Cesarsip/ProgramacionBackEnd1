from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='shift',
            field=models.CharField(
                blank=True,
                default='',
                max_length=20,
                verbose_name='Jornada',
            ),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(
                blank=True,
                default='',
                max_length=30,
                verbose_name='Sexo',
            ),
        ),
    ]
