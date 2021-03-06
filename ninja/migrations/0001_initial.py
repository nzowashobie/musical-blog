# Generated by Django 3.1.1 on 2021-10-02 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Africa_muzik',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=50, null=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=10, null=True)),
                ('audio', models.FileField(upload_to='afrobeat')),
                ('art', models.FileField(upload_to='afrobeat_art')),
            ],
        ),
        migrations.CreateModel(
            name='beats_Z',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=50, null=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=10, null=True)),
                ('audio', models.FileField(upload_to='zedbeat')),
                ('art', models.FileField(upload_to='zedbeat_art')),
            ],
        ),
        migrations.CreateModel(
            name='Catag_hiphop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(max_length=50, null=True, unique=True)),
                ('art', models.FileField(upload_to='hiphop_covers')),
            ],
        ),
        migrations.CreateModel(
            name='Catalbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(max_length=50, null=True, unique=True)),
                ('art', models.FileField(upload_to='covers')),
            ],
        ),
        migrations.CreateModel(
            name='Classic_Hiphop',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=50, null=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=10, null=True)),
                ('audio', models.FileField(upload_to='classic_Hiphop')),
                ('art', models.FileField(upload_to='classic_Hip_art')),
            ],
        ),
        migrations.CreateModel(
            name='Classic_Rnb',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=50, null=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=10, null=True)),
                ('audio', models.FileField(upload_to='classic_RnB')),
                ('art', models.FileField(upload_to='classic_RnB_art')),
            ],
        ),
        migrations.CreateModel(
            name='Classic_zed',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=50, null=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=10, null=True)),
                ('audio', models.FileField(upload_to='classic_zed')),
                ('art', models.FileField(upload_to='classic_zed_art')),
            ],
        ),
        migrations.CreateModel(
            name='gospel',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=50, null=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=10, null=True)),
                ('audio', models.FileField(upload_to='gospel')),
                ('art', models.FileField(upload_to='gospel_art')),
            ],
        ),
        migrations.CreateModel(
            name='Hiphop',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=50, null=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=10, null=True)),
                ('audio', models.FileField(upload_to='Hiphop')),
                ('art', models.FileField(upload_to='Hiphop_art')),
            ],
        ),
        migrations.CreateModel(
            name='hiphop_vid',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=50, null=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=10, null=True)),
                ('video', models.FileField(upload_to='hiphop_videos')),
            ],
        ),
        migrations.CreateModel(
            name='Live',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=50, null=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=10, null=True)),
                ('video', models.FileField(upload_to='videos')),
            ],
        ),
        migrations.CreateModel(
            name='mov',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, null=True)),
                ('comments', models.TextField()),
                ('genre', models.CharField(max_length=10, null=True)),
                ('movie', models.FileField(upload_to='movies')),
                ('poster', models.FileField(upload_to='posters')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('Biography', models.TextField()),
                ('images', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='skool',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100, null=True)),
                ('comments', models.CharField(max_length=1000, null=True)),
                ('file', models.FileField(upload_to='files')),
                ('cover', models.FileField(upload_to='book_cover')),
            ],
        ),
        migrations.CreateModel(
            name='Throw_back',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=50, null=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=10, null=True)),
                ('audio', models.FileField(upload_to='throw_back')),
                ('art', models.FileField(upload_to='throw_art')),
            ],
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=50, null=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=10, null=True)),
                ('audio', models.FileField(upload_to='RnB')),
                ('art', models.FileField(upload_to='RnB_art')),
            ],
        ),
        migrations.CreateModel(
            name='vid',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=50, null=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=10, null=True)),
                ('video', models.FileField(upload_to='videos')),
                ('poster', models.FileField(upload_to='videos_covers')),
            ],
        ),
        migrations.CreateModel(
            name='zed_vid',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=50, null=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=10, null=True)),
                ('video', models.FileField(upload_to='zed_videos')),
                ('poster', models.FileField(upload_to='zed_vidz_covers')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(max_length=50, null=True)),
                ('Artist', models.CharField(max_length=50, null=True)),
                ('Songs', models.FileField(upload_to='albums')),
                ('Title', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=50, null=True)),
                ('year', models.CharField(max_length=50, null=True)),
                ('art', models.FileField(upload_to='albums')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ninja.catalbum')),
            ],
        ),
        migrations.CreateModel(
            name='Hip_hop_abums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(max_length=50, null=True)),
                ('Artist', models.CharField(max_length=50, null=True)),
                ('Songs', models.FileField(upload_to='hiphop_albums')),
                ('Title', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(max_length=50, null=True)),
                ('year', models.CharField(max_length=50, null=True)),
                ('art', models.FileField(upload_to='hiphop_albums_art')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ninja.catag_hiphop')),
            ],
        ),
    ]
