# Election results

It's election night! Exciting! We have a feed of election results from a data supplier. They will supply us a file which will be updated throughout the night as results come in.

## Results format

The fields in the file will be separated by commas but each row will vary in length as described below.

A result will consist of:

A. A constituency
B. A repeating set of pairs with the party code and the votes cast

So for example:

    "Cardiff West, 11014, C, 17803, L, 4923, UKIP, 2069, LD",
    "Islington South & Finsbury, 22547, L, 9389, C, 4829, LD, 3375, UKIP, 3371, G, 309, Ind"

### Codes

* C - Conservative Party
* L - Labour Party
* UKIP - UKIP
* LD - Liberal Democrats
* G - Green Party
* Ind - Independent
* SNP - SNP


## Tasks:
We want to transform this into a cleaned-up result that shows:

1. the constituency name

2. the result for each party

3. find the winner for each constituency

4. translates the party code into a full name

5. shows the share of the vote as a percentage of all the votes cast



## Extension tasks:

### Validation

If loading as a separate CSV file, and there is a problem with the format of the results file then all good entries should result in output and the error should go to a separate error log with the problem explained in non-technical language that a journalist might be able to understand and report back to the results service.

## Enhancements

The results service may be behind the actual results or may contain an error. We want to be able to combine the results file with an "override" file. If a constituency has an entry for a party in the override file that value should be used instead of the result file.

If the constituency is not present in the results file the result should be added entirely from the override file.

## Swing-o-meter

Suppose we have a result file from the previous election in the same format. Add the percentage changes in the vote to the results.

Calculate the average change towards or away from the parties and then use this average swing to predict the result of elections that are in the previous election's result file but not in the current one.

### Extension

Discuss (but do not solve in code) how you would amend this solution to deal with the fact that the number of eligible voters changes from election to election.
