Title: How to move a model between two Django apps
Date: 2018-03-12 20:30
Category: Programming, Django
Tags: django, learning

Let's imagine that you have 2 django apps: `article` and `blog`. 
So first one has model `Article` as you already guessed.
So we need to move our `Article` model from `article` app to `blog` app.

* Copy your code of `Article` model from `article` app to `blog` app into `models.py`.
* We need to specify database table for our moved model. At our example it is `article_article`. 
You need to add to your `blog.Article` model next lines:

```python
class Meta:
    db_table = 'article_article'
```

* Now you can `python manage.py makemigrations blog` for getting django migration for creating model or you could get
creation migration from your `article` app and place it to migrated migration in `blog` app. If you run above command,
you need to delete this migration after place it into previously migrated migration.

* Now you need to change all references in your whole project to new new reference of your model.
It can be ForeignKey, import etc.

* Verify that you do all correctly with command: `./manage.py migrate`. Nothing should be migrated.
If not - verify previous steps, because we just changed place of your model code, not database table name.

* Last step will be remove `db_table` field from `class Meta` and run next command:

```bash
./manage.py makemigrations blog
./manage.py migrate blog
```

After create migration you could see something next operation at migration:

```python
operations = [
        migrations.AlterModelTable(
            name='blog',
            table=None,
        ),
    ]
```

`table=None` means it will take the default table-name, which in this case will be `blog_article`.

This solution was tested with Django 1.11 and Postgres database with ForeignKey relation.

Hope it helps.
