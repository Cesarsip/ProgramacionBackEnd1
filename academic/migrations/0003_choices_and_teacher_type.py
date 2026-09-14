from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_course_shift_student_gender'),
    ]

    operations = [
        # Agrega el tipo de profesor sin borrar registros existentes.
        migrations.AddField(
            model_name='teacher',
            name='teacher_type',
            field=models.CharField(
                choices=[
                    ('CH', 'Jornada por hora'),
                    ('CD', 'Jornada definida'),
                ],
                default='CH',
                max_length=2,
                verbose_name='Tipo de profesor',
            ),
        ),
        migrations.AlterField(
            model_name='course',
            name='shift',
            field=models.CharField(
                choices=[('D', 'Despertino'), ('V', 'Vespertino')],
                default='D',
                max_length=1,
                verbose_name='Jornada',
            ),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(
                choices=[('M', 'Masculino'), ('F', 'Femenino')],
                default='M',
                max_length=1,
                verbose_name='Sexo',
            ),
        ),
    ]
