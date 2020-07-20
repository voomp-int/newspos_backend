# Generated by Django 3.0.8 on 2020-07-20 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('url', models.CharField(max_length=350)),
                ('urlToImage', models.TextField()),
                ('publishedAt', models.DateTimeField()),
                ('compound_score', models.FloatField()),
            ],
            options={
                'db_table': 'articles',
            },
        ),
    ]
