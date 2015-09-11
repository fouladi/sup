SUP
===

A simple translation of Persian (Farsi) in Arabic script (with some
extra letters) to Latin (roman) characters. It uses an many-to-one
mapping between an Arabic characters and their roman correspond. I call
the target format **SUP** (`Simple UniPers`). I got this idea after reading
about `UniPers` in `Wikipedia`.

The Persian (in Arabic script) is written from right to left and the
Latin scripts the other way round. This script converts words as they
come in. If the order is not correct, an next algorithm should change
the order of words in a paragraph.

I have no clue for an appropriate usage. The output maybe only an
intermediate format for other algorithms to further modifications or
normalization, or it may be used in current form for short messages
systems (like SMS) or for logging in an limited embedded system.

Mapping:
--------

The following table shows the mapping of Extended Arabic characters to
their corresponding Latin char.


Extended Arabic | Latin
----------------|------
   ع            |   '
   ،            |   ,
   ۱            |   1
   ۲            |   2
   ۳            |   3
   ۴            |   4
   ۵            |   5
   ۶            |   6
   ۷            |   7
   ۸            |   8
   ۹            |   9
   ؛            |   ;
   ؟            |   ?
   آ   ا        |   a
   ب            |   b
   چ            |   c
   د            |   d
   ف            |   f
   گ            |   g
   ه  ح         |   h
   ی            |   i
   ج            |   j
   ک            |   k
   ل            |   l
   م            |   m
   ن            |   n
   پ            |   p
   غ  ق         |   q
   ر            |   r
   ث   س   ص    |   s
   ت   ط        |   t
   و            |   u
   خ            |   x
   ظ ز  ض   ذ   |   z
   ش            |   š
   ڎ            |   ž

These Latin-1 characters are not mapped:

    e o v w 

Limitation:
-----------

The main limitation of this kind of "transliterartion" is its
irreversibility. It means, after converting a word to the target format
(SUP), the information to converting it back, is lost.

But someone who can read Persian with Arabic characters, can correctly
guess the word in SUP.

A database with hash values of Persian words (with Arabic letters) as
index in a table, could be used for a reverse mapping of a SUP word to
original Persian word (in Arabic letters).

Usage:
------

This script is written in Python 3 and you need Python 3 for using it.

~~~~~

>>> from simple_unipers import deromanize
>>> example = "فارسی"
>>> print(deromanize(example))
farsi
>>> xiam = """
... در کارگه کوزه گری رفتم دوش
...  دیدم دو هزار کوزه گویا و خموش
... ناگاه یکی کوزه براورد خروش
... کو کوزه گر و کوزه خر و کوزه فروش
... """
>>> print(deromanize(xiam))

dr kargh kuzh gri rftm duš
 didm du hzar kuzh guia u xmuš
nagah iki kuzh braurd xruš
ku kuzh gr u kuzh xr u kuzh fruš

>>> 

~~~~~
