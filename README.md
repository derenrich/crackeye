crackeye
========

[Minteye](http://www.minteye.com/) is a new CAPTCHA in a modern trend of weak advertising-based CAPTCHAs (similar to [NuCaptcha](http://www.nucaptcha.com/)). I find these CAPTCHAs frustrating because they monetize what should be free and because they are generally weaker than non-advertising CAPTCHAs.

This program cracks the current version of Minteye. See [the minteye website](http://www.minteye.com/Products.aspx) for an example CAPTCHA. The program works most of the time and when it doesn't it returns a frame close to the correct frame. Some additional tweaking should get 100% accuracy.

The scripts require numpy and the opencv python bindings.

Usage
=====
>$ python fetch.py "http://img0.demo.minteye.com/slider/image.ashx?CaptchaId=&w=300&h=250&dumm=634914060070085927&reqid=32840983-832D-40CF-87B3-AC6A7717C5A7&img="

>$ python eval.py *.jpeg

>Best guess: 22.jpeg
