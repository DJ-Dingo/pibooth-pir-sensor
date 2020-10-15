
====================
pibooth-pir-sensor
====================

|PythonVersions| |PypiPackage| |Downloads|

``pibooth-pir-sensor`` is a plugin for the `pibooth`_ application.

.. image:: https://raw.githubusercontent.com/DJ-Dingo/pibooth-pir-sensor/master/templates/pir.png
   :align: center
   :alt: PIR sensor


PIR sensor for Pibooth. It plays a random sound & turn on a light when there are motion. It runs automatic after a 2 minute countdown period without any motion has expired.
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


States description
------------------

 

Circuit diagram
---------------

Wiring
------

.. image:: https://raw.githubusercontent.com/DJ-Dingo/pibooth-pir-sensor/master/templates/pir-sensor-wirring.png
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
