# Authorship Analysis

Our team in Trello is *Group D*.
 
This repository contains the following contents;
 
* Source code - *auth.py*
* Data set - *gutenberg*
* Result text - *result.txt*

## What the program does

This program takes two *known text* and one *questioned text*. Then, it computes the log-likelihood function and decides which of two text is near to questioned text.

 
## Execution Step

**Step1:** Make sure that the source code(*auth.py*) and data set(*gutenberg*) are in the same directory.

**Step2:** Run the following command in terminal with any file name in the data set;
```
python3 auth.py filename1 filename2 filename3
```

Note: The `filename1` and `filename2` correspond to the *known text* and `filename3` corresponds to the *questioned text*.

For example,
```
python3 auth.py austen-emma.txt shakespeare-caesar.txt austen-sense.txt
```

In this case, the known texts are *austen-emma.txt* and *shakespeare-caesar.txt*, the questioned text is *austen-sense.txt*.

**Step3:** The result is shown in the *result.txt* with the value of log-likelihood function for each *known text*.

Note: The result already shown from the beginning is by the example of Step2.


## Reference

1. https://thecleverprogrammer.com/2021/01/01/authorship-attribution-with-python/
