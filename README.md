sup
===

A simple translation of Persian (Farsi) in Arabic script (with some
extra letters) to Latin (roman) characters. It uses an many-to-one
mapping between an Arabic characters and their roman correspond. I call
the target format SUP (Simple UniPers). I got this idea after reading
about `UniPers` in `Wikipedia`.

The Persian (in Arabic script) is written from right to left and the
Latin scripts the other way round. This script converts words as they
come in. If the order is not correct, an next algorithm should change
the order of words in a paragraph.

I have no clue for an appropriate usage. The output maybe only an
intermediate format for other algorithms to further modifications or
normalization, or it may be used in current form for short messages
systems (like SMS) or for logging in an limited embedded system.


Limitation:
-----------

The main limitation of this kind of "transliterartion" is its
irreversibility. It means, after converting a word to the target format
(SUP), the information to converting it back, is lost.


Usage:
------

This script is written in Python 3 and you need Python 3 for using it.

~~~~~

>>> import simple_unipers
>>> example = "فارسی"
>>> print(simple_unipers.deromanize(example))
farsi

~~~~~
