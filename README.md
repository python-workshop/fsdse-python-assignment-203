# Given a positive integer, get the next largest number and the next smallest number with the same number of 1's as the given number.

## Constraints
* Is the output a positive int?
    * Yes
* Can we assume the inputs are valid?
    * No
* Can we assume this fits memory?
    * Yes

## Algorithm
* Find the right-most non trailing zero, call this index
* We'll use a mask of 1 and do a logical right shift on a copy of num to examine each bit starting from the right
* Count the number of zeroes to the right of index
    * While num & 1 == 0 and num_copy != 0:
        * Increment number of zeroes
        * Logical shift right num_copy
* Count the number of ones to the right of index
    * While num & 1 == 1 and num_copy != 0:
        * Increment number of ones
        * Logical shift right num_copy
* The index will be the sum of number of ones and number of zeroes
* Set the index bit
* Clear all bits to the right of index
* Set bits starting from 0
    * Only set (number of ones - 1) bits because we set index to 1

__NOTE__ - We should make a note that Python does not have a logical right shift operator built in. We can either use a positive number of implement one for a 32 bit number: