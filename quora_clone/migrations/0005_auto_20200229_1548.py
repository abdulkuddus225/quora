# Generated by Django 2.2.6 on 2020-02-29 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quora_clone', '0004_auto_20200229_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='question_id',
            new_name='answer_id',
        ),
        migrations.CreateModel(
            name='QuesAns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quora_clone.Answers')),
                ('Questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quora_clone.Questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
