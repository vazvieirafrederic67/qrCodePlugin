=====
qrCodePlugin
=====



Quick start
-----------

1. Add "qrCodePlugin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'qrCodePlugin',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('qrCode/', include('cms.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/qrCode/ to participate in the qrCodePlugin.