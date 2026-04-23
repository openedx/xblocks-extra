Qualtrics Survey
================

.. note::
   This XBlock is part of the `xblocks-extra <https://github.com/openedx/xblocks-extra>`_ collection.

An XBlock to ease linking to Qualtrics surveys.

The tool makes it easy for instructors to link to a Qualtrics survey
from within their course.


Installation
------------

System Administrator
~~~~~~~~~~~~~~~~~~~~

To install the XBlock on your platform, you will need to install the package collection it belongs to.
Add the following to your platform's ``requirements.txt`` file:

    xblocks-extra

You may also need to ensure this is in your ``INSTALLED_APPS``:

    qualtricssurvey


Course Staff
~~~~~~~~~~~~

To enable the XBlock in your course,
access your `Advanced Module List`:

    Settings -> Advanced Settings -> Advanced Module List

and add the following:

    qualtricssurvey


Use
---

Course Staff
~~~~~~~~~~~~

To add a Qualtrics Survey link to your course:

- go to a unit in Studio
- select "Qualtrics Survey" from the Advanced Components menu

You can now edit and preview the new component.

Using the Studio editor, you can edit the following fields:

- display name
- survey id
- university
- link text
- extra parameters
- message

Configuration
~~~~~~~~~~~~~

Operators can configure system-wide defaults via ``XBLOCK_SETTINGS`` in
the Django settings:

.. code-block:: python

    XBLOCK_SETTINGS["QualtricsSurvey"] = {
        "DEFAULT_UNIVERSITY": "stanforduniversity",
        "USER_QUERY_PARAMS": {
            "edxuid": "user_id",
            "email": "email",
        },
    }

``DEFAULT_UNIVERSITY``
    The default Qualtrics subdomain for your institution. Used when the
    per-instance university field is left blank.

``USER_QUERY_PARAMS``
    A mapping of URL parameter names to user attributes. The key is the
    query parameter name that appears in the survey URL, and the value is
    the user attribute to resolve. Supported attributes:

    - ``user_id`` - platform user ID (with fallback to anonymous ID)
    - ``anonymous_id`` - anonymous student identifier
    - ``email`` - primary email address
    - ``username`` - platform username

    If ``USER_QUERY_PARAMS`` is not configured, no user parameters are
    sent by default. To start sending user data to Qualtrics, operators
    must explicitly configure this setting.
    Existing blocks that already store a legacy ``param_name`` value
    continue to use that value as a fallback.


Participants
~~~~~~~~~~~~

Students click on a link within the unit and this takes them to the survey.
