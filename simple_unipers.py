#! /usr/bin/env python3
# vim: set fileencoding=utf-8
# Description: converting persian with arabic alphabet to roman alphabet
#   This conversion based on the "Simple Unipers" coding format. Each
#   extended arabic character will be converted to one specific roman
#   characters. The association will be N:1! It means more than one
#   arabic chars can be mapped to one roman char.
#
#   The input text should be in persian "utf-8" with extended arabic alphabet.
#   The output text will be in roman characters.
# Author: Farhad Fouladi 2015

# A_hat = '\N{LATIN CAPITAL LETTER A WITH CIRCUMFLEX}'
# a_hat = '\N{LATIN SMALL LETTER A WITH CIRCUMFLEX}'
Z_hat = '\N{LATIN CAPITAL LETTER Z WITH CARON}'
z_hat = '\N{LATIN SMALL LETTER Z WITH CARON}'
S_hat = '\N{LATIN CAPITAL LETTER S WITH CARON}'
s_hat = '\N{LATIN SMALL LETTER S WITH CARON}'

arab_alef       = '\N{ARABIC LETTER ALEF}'
arab_alef_madda = '\N{ARABIC LETTER ALEF WITH MADDA ABOVE}'
arab_beh        = '\N{ARABIC LETTER BEH}'
arab_peh        = '\N{ARABIC LETTER PEH}'
arab_teh        = '\N{ARABIC LETTER TEH}'
arab_theh       = '\N{ARABIC LETTER THEH}'
arab_jeem       = '\N{ARABIC LETTER JEEM}'
arab_tcheh      = '\N{ARABIC LETTER TCHEH}'
arab_hah        = '\N{ARABIC LETTER HAH}'
arab_khah       = '\N{ARABIC LETTER KHAH}'
arab_dal        = '\N{ARABIC LETTER DAL}'
arab_thal       = '\N{ARABIC LETTER THAL}'
arab_reh        = '\N{ARABIC LETTER REH}'
arab_zain       = '\N{ARABIC LETTER ZAIN}'
arab_dul        = '\N{ARABIC LETTER DUL}'
arab_seen       = '\N{ARABIC LETTER SEEN}'
arab_sheen      = '\N{ARABIC LETTER SHEEN}'
arab_sad        = '\N{ARABIC LETTER SAD}'
arab_dad        = '\N{ARABIC LETTER DAD}'
arab_tah        = '\N{ARABIC LETTER TAH}'
arab_zah        = '\N{ARABIC LETTER ZAH}'
arab_ain        = '\N{ARABIC LETTER AIN}'
arab_ghain      = '\N{ARABIC LETTER GHAIN}'
arab_feh        = '\N{ARABIC LETTER FEH}'
arab_qaf        = '\N{ARABIC LETTER QAF}'
arab_keheh      = '\N{ARABIC LETTER KEHEH}'
arab_gaf        = '\N{ARABIC LETTER GAF}'
arab_lam        = '\N{ARABIC LETTER LAM}'
arab_meem       = '\N{ARABIC LETTER MEEM}'
arab_noon       = '\N{ARABIC LETTER NOON}'
arab_waw        = '\N{ARABIC LETTER WAW}'
arab_heh        = '\N{ARABIC LETTER HEH}'
arab_yeh        = '\N{ARABIC LETTER FARSI YEH}'
arab_quest      = '\N{ARABIC QUESTION MARK}'
arab_comma      = '\N{ARABIC COMMA}'
arab_semi       = '\N{ARABIC SEMICOLON}'
arab_0          = '\N{EXTENDED ARABIC-INDIC DIGIT ZERO}'
arab_1          = '\N{EXTENDED ARABIC-INDIC DIGIT ONE}'
arab_2          = '\N{EXTENDED ARABIC-INDIC DIGIT TWO}'
arab_3          = '\N{EXTENDED ARABIC-INDIC DIGIT THREE}'
arab_4          = '\N{EXTENDED ARABIC-INDIC DIGIT FOUR}'
arab_5          = '\N{EXTENDED ARABIC-INDIC DIGIT FIVE}'
arab_6          = '\N{EXTENDED ARABIC-INDIC DIGIT SIX}'
arab_7          = '\N{EXTENDED ARABIC-INDIC DIGIT SEVEN}'
arab_8          = '\N{EXTENDED ARABIC-INDIC DIGIT EIGHT}'
arab_9          = '\N{EXTENDED ARABIC-INDIC DIGIT NINE}'

multi_map = str.maketrans({
    arab_alef  : 'a',
    arab_alef_madda  : 'a',
    arab_beh   : 'b',
    arab_peh   : 'p',
    arab_teh   : 't',
    arab_theh  : 's',
    arab_jeem  : 'j',
    arab_tcheh : 'c',
    arab_hah   : 'h',
    arab_khah  : 'x',
    arab_dal   : 'd',
    arab_thal  : 'z',
    arab_reh   : 'r',
    arab_zain  : 'z',
    arab_dul   : z_hat,
    arab_seen  : 's',
    arab_sheen : s_hat,
    arab_sad   : 's',
    arab_dad   : 'z',
    arab_tah   : 't',
    arab_zah   : 'z',
    arab_ain   : "'",
    arab_feh   : 'f',
    arab_ghain : 'q',
    arab_keheh : 'k',
    arab_qaf   : 'q',
    arab_gaf   : 'g',
    arab_lam   : 'l',
    arab_meem  : 'm',
    arab_noon  : 'n',
    arab_waw   : 'u',
    arab_heh   : 'h',
    arab_yeh   : 'i',
    arab_quest : '?',
    arab_comma : ',',
    arab_semi  : ';',
    arab_1: '1',
    arab_2: '2',
    arab_3: '3',
    arab_4: '4',
    arab_5: '5',
    arab_6: '6',
    arab_7: '7',
    arab_8: '8',
    arab_9: '9',
})


def deromanize(txt):
    """replace persian symbols with roman chars"""
    return txt.translate(multi_map)


if __name__ == '__main__':
    example = "فارسی باستان در کنار زبان اوستایی تنها زبانهای ایرانی دوران کهن هستند که متن یا کتیبههایی از آنها به جا مانده است."
    print(example)
    print(deromanize(example))
