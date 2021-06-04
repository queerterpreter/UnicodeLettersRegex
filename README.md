# Unicode Letters Regex
## Hello!
I'm a corpus linguist who often deals with texts with special characters standing in for letters. Aside from not being accessible for screen readers, they wreck my analysis because "Hello" and "𝓗ello" are different words from the computer's point of view.

While there are a couple sites out there that will clean specific lines, I'm dealing with huge files and I needed to automate it. Enter some unelegant regexes. My unscientific approach was going to several "fancy font" generators and compiling all the fonts into one document, so I'm sure I'm missing some not-actually-letters here. I'm sure it's non-exhaustive, so please add away if you find characters I missed.

## Setup etc
I'm honestly just learning how to use Python so it's hekkin simple. **You need Python 3 or above**, or else (ironically?) it won't be able to deal with the non-ASCII characters. That's all there is to it, boot it up and tell it where to find the .txt file(s). Happy cleaning!
