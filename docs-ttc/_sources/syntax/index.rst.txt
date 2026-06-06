Syntax
===========

In ttc, we'll use an extension of the SMT-LIB syntax to express counting problems.

We'll add two new commands to the SMT-LIB syntax:
- `(declare-projvar <varlist>)`: This command declares a variable as a projection variable. The counting will be done over the projection variables.
- `(declare-weight <var> <weight>)`: This command declares a variable as a weight variable. The counting will be done with the weights of the weight variables.

.. code-block:: scheme

   (set-logic QF_UFBV)
   (declare-const x (_ BitVec 8))
   (declare-const y (_ BitVec 8))
   (declare-projvar x)
   (declare-weight x 0.1)
   (assert (= x #x0a))
   (check-sat)