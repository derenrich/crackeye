crackeye
========

Simple python library to break minteye CAPTCHAs

See http://www.minteye.com/Products.aspx for an example of a CAPTCHA this is designed to crack

Requires numpy and the opencv python bindings.

Usage
=====

$ python fetch.py "http://img0.demo.minteye.com/slider/image.ashx?CaptchaId=&w=300&h=250&dumm=634914060070085927&reqid=32840983-832D-40CF-87B3-AC6A7717C5A7&img="
$ python eval.py *.jpeg
Best guess: 22.jpeg
