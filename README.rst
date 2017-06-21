example-rb-oauth2-client
========================


Installation
------------

In a clean virtual environment:


.. code-block:: shell

   ./setup.py develop
   cp contrib/settings_local.example.py example_client/settings_local.py
   $EDITOR example_client/settings_local.py  # Fill in your Review Board details.
   ./manage.py migrate
   ./manage.py makesuperuser  # Optional
   ./manage.py runserver
