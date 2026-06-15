Function Counting
=================

Engine 4 counts the interpretations (Skolem functions) of an uninterpreted
function that satisfy a formula, using SkolemFC. It is intended for ``QF_UFBV``
formulas that constrain the behaviour of an uninterpreted function.

By default the function named ``mainfunc`` is counted; use ``--func`` to choose
another. The example below counts how many 12-bit-to-12-bit functions encode a
valid non-trivial factorization:

.. code-block:: smtlib

   (set-logic QF_UFBV)

   (declare-const w (_ BitVec 12))
   (declare-fun mainfunc ((_ BitVec 12)) (_ BitVec 12))

   (define-fun out () (_ BitVec 12) (mainfunc w))
   (define-fun x   () (_ BitVec 6)  ((_ extract  5 0) out))
   (define-fun y   () (_ BitVec 6)  ((_ extract 11 6) out))

   ; avoid trivial factors
   (assert (bvugt x (_ bv1 6)))
   (assert (bvugt y (_ bv1 6)))

   ; the output must be a valid factorization of w
   (assert (= w (bvmul ((_ zero_extend 6) x) ((_ zero_extend 6) y))))

   (check-sat)

Options
-------

``--skolemfc``
   Force engine 4 (uninterpreted-function counting).

``--func <name>``
   Name of the uninterpreted function to count (default: ``mainfunc``).
