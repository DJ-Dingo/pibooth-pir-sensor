.. role:: raw-html(raw)
    :format: html
====================
pibooth-pir-sensor
====================

|PythonVersions| |PypiPackage| |Downloads|

``pibooth-pir-sensor`` is a plugin for the `pibooth`_ application.

.. image:: https://raw.githubusercontent.com/DJ-Dingo/pibooth-pir-sensor/master/templates/pir-sensors.png
   :align: center
   :alt: PIR sensor


PIR sensor for Pibooth. :raw-html:`<br />` 
It plays a random sound & turn on a light when there are motion. :raw-html:`<br />`
If someone activate the PIR-sensor, after a 2 minute countdown period has expired without any motion. :raw-html:`<br />`
That way it can turn on a light, and say "Hello, wanna take a photo" too a person if they walk by the Pibooth Selfiecam.

This is not a plugin yet, run it in the background.


--------------------------------------------------------------------------------

Adds an PIR sensor to the pibooth



Install
-------

::


Configuration
-------------

.. image:: https://raw.githubusercontent.com/DJ-Dingo/pibooth-pir-sensor/master/templates/pir-sensor-info_.png
   :align: center
   :alt: PIR-sensor info

Most commen PIR-sensors hc-sr501, hc-sr505 Mini :raw-html:`<br />`
Here we use an hc-sr501, but it works with any PIR-sensor

- Set the jumper to single trigger.
- Set the delay all the way to the left 0.3 sec.
- Set the Sensitivity/Distance all the way to the right. (lower it if you need to, or use trick 1 or 2).


Tricks to make PIR, less sensitive but still respond.
- There are 2 things you can do. First take off the Fresnel Lens "white plastic cover".

.. image:: https://raw.githubusercontent.com/DJ-Dingo/pibooth-pir-sensor/master/templates/pir-sensor-no-shield2.png


1. Take an old ball pen and use the plastic or rubber part by putting it over the PIR sensor, to make the PIR work more direct.
2. Or fill the Fresnel Lens "white plastic cover" with some paper towel or tin foil, except for a small hole. 
   IMPORTENT, make shure the tin foil does not have contact with the circuit board.


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


To prevent false motion, you can use a Clip Ferrite around the 3 wire, or solder one between the wire VCD and again one between the wire and OUT.

.. image:: https://github.com/DJ-Dingo/pibooth-pir-sensor/blob/master/templates/ferrite_.png
   :align: center
   :alt:  PIR-sensor Wirring


.. --- Links ------------------------------------------------------------------

.. _`pibooth`: https://pypi.org/project/pibooth

.. |PythonVersions| image:: https://img.shields.io/badge/python-2.7+ / 3.6+-red.svg
   :target: https://www.python.org/downloads
   :alt: Python 2.7+/3.6+
