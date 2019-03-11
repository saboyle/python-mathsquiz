# Mathsquiz

A minimal maths testing / learning utility.

Enables a quick and easy set of customizable match questions 
to be generated and marked.

Initially written to help Key Stage 1 and Key Stage 2 maths
practice.

Additional levels of difficulty can easily be generated by 
sub-classing the Quiz class.  Operators can be constrained to
1 or more of ['+', '-', '*', '/'].

Specific Times Tables can be exercised by passing a fix_number
parameter on the end of the invocation.

Example executions:
```bash
python quiz.py run --name=Steve 
                   --max_number=100 
                   --num_questions=10
```

```bash
# To test 2 times table (only on multiplications).
python quiz.py run --name=Steve 
                   --max_number=10
                   --num_questions=10
                   --fix_number=2
```
## Available parameters:

```bash
Usage:       quiz.py - 
             quiz.py - allow-negative-numbers
             quiz.py - fix-number
             quiz.py - max-number
             quiz.py - min-number
             quiz.py - name
             quiz.py - num-questions
             quiz.py - operators
             quiz.py - run
```