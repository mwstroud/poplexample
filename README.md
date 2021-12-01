# poplexample

This repository tries to be a compact testing environment for antlr and uses example code and information from the following sources:
References

• https://tomassetti.me/antlr-mega-tutorial/

• https://jason.whitehorn.us/blog/2021/02/08/getting-started-withantlr-for-python/

• https://dzone.com/articles/antlr-4-with-python-2-detailed-example

• https://faun.pub/introduction-to-antlr-python-af8a3c603d23

• https://gist.github.com/jeroendeswaef/563cd2ab68ab895aedff

• https://github.com/antlr/grammars-v4


This code has a example_grammar.g4 grammar file, a runtime.py file to run the antlr generated Parser and Lexer, and an input.txt file containing the code to be parsed.

This repository is just to make sure your environment is set up correctly to run antlr4 and has the correct python runtime environment.
This is also a skeleton to start working on your own parser. 

Start by downloading the Java 17 jdk version or greater.

Then download the .jar file from antlr4.

Then I used an anaconda environment to run:

```
pip install antlr4-python3-runtime
```
Then I ran the antlr .jar file on the .g4 grammar file  (I had to mess around with environment variables until it worked).
This generated the .interp files , .tokens files, and the lexer.py, parser.py, and listener.py. 

As far as making a Lexer and Parser, you are done!

Then to test it, you need to run the "runtime.py" script as follows

```
python runtime.py < input.txt
```

This tutorial goes through a lot more information
https://faun.pub/introduction-to-antlr-python-af8a3c603d23
