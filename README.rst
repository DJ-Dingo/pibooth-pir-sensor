
====================
pibooth-pir-sensor
====================

|PythonVersions| |PypiPackage| |Downloads|

``pibooth-pir-sensor`` is a plugin for the `pibooth`_ application.

.. image:: https://raw.githubusercontent.com/DJ-Dingo/pibooth-pir-sensor/master/templates/pir-sensors.png
   :align: center
   :alt: PIR sensor


PIR sensor for Pibooth. It plays a random sound & turn on a light when there are motion. It runs automatic if someone activate the PIR-sensor, after a 2 minute countdown period has expired without any motion. That way it can turn on a light, and say "Hello, wanna take a photo" too a person if they walk by the Pibooth Selfiecam.

This is not a plugin yet, run it in the background.


--------------------------------------------------------------------------------

Adds an PIR sensor to the pibooth



Install
-------

::


Configuration
-------------

.. image:: https://raw.githubusercontent.com/DJ-Dingo/pibooth-pir-sensor/master/templates/pir-sensor-info.png
   :align: center
   :alt: PIR-sensor info

Most commen PIR-sensors hc-sr501, hc-sr505 Mini

- Here we use an hc-sr501, but it works with any PIR-sensor

- Set the jumper to single trigger.
- Set the delay all the way to the left 0.3 sec.
- Set the Sensitivity/Distance all the way to the right. (lower it if you need to, or use trick 1 or 2).

Tricks to make PIR, less sensitive but still respond.

- There are 2 things you can do. Take off the white plastic shield.

.. image:: https://raw.githubusercontent.com/DJ-Dingo/pibooth-pir-sensor/master/templates/pir-sensor-no-shield.png


1. Take an old pen and use the plastic part by putting it over the PIR sensor, to make the PIR work more directly
2. Or fill the white plastic shield, except for a small hole


States description
------------------

 

Circuit diagram
---------------

Wiring
------

.. image:: https://github.com/DJ-Dingo/pibooth-pir-sensor/blob/master/templates/pir-sensor-wirring.png
   :align: center
   :alt:  PIR-sensor Wirring

- VCC: Pin   (3V or 5v)
- OUT: Pin   (OUT)
- GND: Pin   (GND)


.. --- Links ------------------------------------------------------------------

.. _`pibooth`: https://pypi.org/project/pibooth

.. |PythonVersions| image:: https://img.shields.io/badge/python-2.7+ / 3.6+-red.svg
   :target: https://www.python.org/downloads
   :alt: Python 2.7+/3.6+
