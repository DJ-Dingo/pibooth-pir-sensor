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

.. contents::

Requirements
------------

Hardware
^^^^^^^^

* 1 Raspberry Pi 3 Model B (or higher) :raw-html:`<br />`
* 1 PIR sensor hc-sr501 or hc-sr505 Mini (but any PIR will work) :raw-html:`<br />`
* 2 Ferrite 2810138-50r-10 (you can also use hf30acb321611-t) :raw-html:`<br />`
*   Or as we done in this project 1 Clip On Soft Ferrite Ring, around all 3 wire  :raw-html:`<br />`
* 1 LED  :raw-html:`<br />`
* 2 Resistors 1 x 100 Ohm, 1 x 1k Ohm  :raw-html:`<br />`

Install
-------

:: This is not a plugin yet, run it in the background.

:: How to Setup comming soon


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

Tricks
^^^^^^
Tricks to make PIR, less sensitive but still respond. There are 2 things you can do. :raw-html:`<br />`
First take off the Fresnel Lens "white plastic cover".

1. Take an old ball pen and use the plastic or rubber part by putting it over the PIR sensor, to make the PIR work more direct.
2. Or fill the Fresnel Lens "white plastic cover" with some paper towel or tin foil, except for a small hole.  :raw-html:`<br />`
   IMPORTANT, make shure the tin foil does not have contact with the circuit board.


.. image:: https://raw.githubusercontent.com/DJ-Dingo/pibooth-pir-sensor/master/templates/pir-sensor-no-shield2.png
   :align: center
   :alt:  PIR-sensor no shield


States description
------------------
Missing Picture

 

Circuit diagram
---------------
Here is the diagram for hardware connections.

.. image:: https://github.com/DJ-Dingo/pibooth-pir-sensor/blob/master/templates/Pibooth-Pir-Sensor%20Sketch_2__bb.png
   :align: center
   :alt:  PIR-sensor Electronic sketch

Wiring
------
PIR - look at your PIR for correct details

- VCC: Pin      (3V or 5v)
- OUT: Pin-GPIO (OUT) - If you use 5v, you should use a resister R2, 1K ohm between OUT and GPIO on your Rpi.
- GND: Pin      (GND)

Ferrite
^^^^^^^
To prevent **false motion**, you can use Ferrite etc a **Clip On Soft Ferrite Ring** around the 3 wire  :raw-html:`<br />` 

.. image:: https://github.com/DJ-Dingo/pibooth-pir-sensor/blob/master/templates/ferrite_pir.png
   :align: center
   :alt:  PIR-sensor Wirring

Or you can solder a Ferrite **2810138-50r-10** or **hf30acb321611-t** between the wire from the GPIO and VCC on the PIR  :raw-html:`<br />`
And again a Ferrite **2810138-50r-10** or **hf30acb321611-t** between the wire from the GPIO and OUT on the PIR.

.. image:: https://github.com/DJ-Dingo/pibooth-pir-sensor/blob/master/templates/ferrite_.png
   :align: center
   :alt:  Ferrite-Info


.. --- Links ------------------------------------------------------------------

.. _`pibooth`: https://pypi.org/project/pibooth

.. |PythonVersions| image:: https://img.shields.io/badge/python-2.7+ / 3.6+-red.svg
   :target: https://www.python.org/downloads
   :alt: Python 2.7+/3.6+
