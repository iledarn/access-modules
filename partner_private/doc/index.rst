=================
 Partner Private
=================

Installation
============

* `Install <https://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html>`__ this module in a usual way

Configuration
=============

* first of all, you should have access to ``Customers`` menu. This menu can be activated for example by installing the ``sale`` module or ``contacts``
* assumed the `sale` module is installed

 * `Log in as SUPERUSER <https://odoo-development.readthedocs.io/en/latest/odoo/usage/login-as-superuser.html>`__
 * `Activate Developer Mode <https://odoo-development.readthedocs.io/en/latest/odoo/usage/debug-mode.html>`__
 * open menu ``[[ Settings ]] >> Users >> Users``
 * choose your `Administrator` user to edit
 * on the form set **[x] Addresses in Sales Orders** and click ``[Save]`` button. This is needed because otherwise you couldn't change partner's type (set it Private, in our case)
 * open menu ``[[ Sales ]] >> Sales >> Customers``
 * choose the customer you need to be private
 * on the form choose ``Address Type -> Private Address``. Note: If you don't see such field, temporary define a **Company**. Then make the partner private and flush **Company** if you don't need it.

Usage
=====

* Create a user for testing
* Open menu ``[[ Settings ]]>> Users >> Users`` and select your user to edit
* On the form choose ``Sales -> Manager``
* Log in using your testing user account
* Open menu ``[[ Sales ]] >> Sales >> Customers``, deactivate ``Customers`` filter.
* RESULT: You should not see your private contact in the list
