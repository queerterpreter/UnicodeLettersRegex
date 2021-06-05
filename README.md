# Unicode Letters Regex
## Hello!
I'm a corpus linguist who often deals with texts with special characters standing in for letters. Aside from not being accessible for screen readers, they wreck my analysis because "Hello" and "𝓗ello" are different words from the computer's point of view.

While there are a couple sites out there that will clean specific lines, I'm dealing with huge files and I needed to automate it. Enter some unelegant regexes. My unscientific approach was going to several "fancy font" generators and compiling all the fonts into one document, so I'm sure I'm missing some not-actually-letters here. I'm sure it's non-exhaustive, so please add away if you find characters I missed.

## Setup etc
**Run in Python 3 or above**, otherwise (ironically?) Python won't be able to deal with the non-ASCII characters. This is set up with relative paths, so you can either put the .txt documents to clean in the "Directory" directory or write in your own path.

Since I already had an iterator script to clean all documents in a directory, I cleaned it up a bit and tossed it here too.

## "Fonts" in RegEx
unicodeletters.txt includes all the characters in the regex, sorted by letter rather than by "font." The "fonts" included are below; again, this is probably non-exhaustive and I welcome additions. The letters excluded aren't my doing, [they were requested over a decade ago](https://unicode.org/wg2/docs/n4068.pdf) but are still not encoded.

LOWERCASE
* Parenthesized Latin Small Letter
* Circled Latin Small Letter
* Mathematical Bold Small
* Mathematical Bold Italic Small
* Mathematical Bold Script Small
* Mathematical Double-Struck Small
* Mathematical Bold Fraktur Small
* Mathematical Sans-Serif Small
* Mathematical Sans-Serif Bold Small
* Mathematical Sans-Serif Italic Small
* Mathematical Sans-Serif Bold Italic Small
* Mathematical Monospace Small
* Fullwidth Latin Small Letter
* Modifier Letter Small (Excludes Q)
* Latin Subscript Small Letter (Excludes B, C, D, F, G, Q, W, Y, and Z)
* Mathematical Italic Small
* Mathematical Script Small
* Mathematical Fraktur Small

UPPERCASE
* Parenthesized Latin Capital Letter
* Circled Latin Capital Letter
* Mathematical Bold Capital
* Mathematical Bold Italic Capital
* Mathematical Bold Script Capital
* Mathematical Double-Struck Capital
* Mathematical Bold Fraktur Capital
* Mathematical Sans-Serif Capital
* Mathematical Sans-Serif Bold Capital
* Mathematical Sans-Serif Italic Capital
* Mathematical Sans-Serif Bold Italic Capital
* Mathematical Monospace Capital
* Squared Latin Capital Letter
* Negative Circled Latin Capital Letter
* Negative Squared Latin Capital Letter
* Fullwidth Latin Capital Letter
* Latin Letter Small Capital (Excludes Q and X)
* Modifier Letter Capital (Excludes C, F, Q, S, X, Y, and Z)
* Mathematical Italic Capital
* Mathematical Script Capital
* Mathematical Fraktur Capital