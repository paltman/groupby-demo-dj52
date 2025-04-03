# Demo of Group By Aggregations Breaking in Django 5.2

## UPDATE
PR that resolves this:
https://github.com/django/django/pull/19334


## Setup

```
docker compose build
docker compose up -d
docker exec -it demo-django python manage.py migrate
docker exec -it demo-django python manage.py loaddata demo/fixtures/orders.json
```

## Reproduce Issue
```
django exec -it demo-django python manage.py shell
>>> from demo.queries import dry_tons
>>> print(dry_orders.query)
```

That should print out a pretty simple group by query with a sum.  But it throws an exception.

This works in <5.2 but after upgrading to 5.2 it throws an error:


```
>>> print(dry_tons.query)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/usr/local/lib/python3.13/site-packages/django/db/models/sql/query.py", line 342, in __str__
    sql, params = self.sql_with_params()
                  ~~~~~~~~~~~~~~~~~~~~^^
  File "/usr/local/lib/python3.13/site-packages/django/db/models/sql/query.py", line 350, in sql_with_params
    return self.get_compiler(DEFAULT_DB_ALIAS).as_sql()
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/usr/local/lib/python3.13/site-packages/django/db/models/sql/compiler.py", line 765, in as_sql
    extra_select, order_by, group_by = self.pre_sql_setup(
                                       ~~~~~~~~~~~~~~~~~~^
        with_col_aliases=with_col_aliases or bool(combinator),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/usr/local/lib/python3.13/site-packages/django/db/models/sql/compiler.py", line 85, in pre_sql_setup
    self.setup_query(with_col_aliases=with_col_aliases)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/site-packages/django/db/models/sql/compiler.py", line 74, in setup_query
    self.select, self.klass_info, self.annotation_col_map = self.get_select(
                                                            ~~~~~~~~~~~~~~~^
        with_col_aliases=with_col_aliases,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/usr/local/lib/python3.13/site-packages/django/db/models/sql/compiler.py", line 286, in get_select
    expression = cols[expression]
                 ~~~~^^^^^^^^^^^^
IndexError: tuple index out of range
```
