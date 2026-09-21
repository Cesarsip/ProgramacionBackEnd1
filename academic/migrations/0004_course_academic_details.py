from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0003_choices_and_teacher_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(
                default='ASIG-000',
                max_length=12,
                verbose_name='Código de asignatura',
            ),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(
                blank=True,
                default='',
                verbose_name='Descripción',
            ),
        ),
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.PositiveSmallIntegerField(
                default=6,
                verbose_name='Créditos',
            ),
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.PositiveSmallIntegerField(
                default=1,
                verbose_name='Semestre',
            ),
        ),
    ]
