# SUP

A simple translation of Persian (`Farsi`) in Arabic script (with a few
extra letters) to Latin (Roman) characters. It uses a many-to-one
mapping between an Arabic character and its Roman equivalent. I call the
target format **SUP** (for `Simple UniPers`). I got the idea after
reading about UniPers in Wikipedia.

The Persian (in Arabic script) is written from right to left and the
Latin scripts the other way round. This script converts words as they
come in. If the order is not correct, a next algorithm should change the
order of words in a paragraph.

I have no idea how to use it. The output may just be an intermediate
format for other algorithms for further modification or normalisation,
or it may be used in its current form for short messaging systems (like
SMS or instant messaging) or for logging in a limited embedded system.

## Mapping:

The following table illustrates the mapping of extended Arabic
characters, which are employed in Farsi, to their corresponding Latin
characters.

| Extended Arabic | Latin | 
| :-------------: | :---: |
|    ع            |   '   |  
|    ،            |   ,   |
|    ۱            |   1   |
|    ۲            |   2   |
|    ۳            |   3   |
|    ۴            |   4   |
|    ۵            |   5   |
|    ۶            |   6   |
|    ۷            |   7   |
|    ۸            |   8   |
|    ۹            |   9   |
|    ؛            |   ;   |
|    ؟            |   ?   |
|    آ   ا        |   a   |
|    ب            |   b   |
|    چ            |   c   |
|    د            |   d   |
|    ف            |   f   |
|    گ            |   g   |
|    ه  ح         |   h   |
|    ی            |   i   |
|    ج            |   j   |
|    ک            |   k   |
|    ل            |   l   |
|    م            |   m   |
|    ن            |   n   |
|    پ            |   p   |
|    غ  ق         |   q   |
|    ر            |   r   |
|    ث   س   ص    |   s   |
|    ت   ط        |   t   |
|    و            |   u   |
|    خ            |   x   |
|    ظ ز  ض   ذ   |   z   |
|    ش            |   š   |
|    ڎ            |   ž   |

These Latin-1 characters are not mapped:

```
    e o v w 
```

## Limitation:

The main issue with this kind of "transliteration" is that it's not
reversible. Once you've converted a word to the target format (SUP), you
can't go back to the original.

But someone who can read Persian with Arabic characters can still guess
the word in SUP.

One solution could be to create a database with hash values of Persian
words (with Arabic letters) as index in a table, so you can reverse map
a SUP word to the original Persian word (in Arabic letters).

## Usage:

This script is written in Python 3 and you need Python 3 for using it.

```
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
```
