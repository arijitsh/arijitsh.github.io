Hybrid Formulas
===============

Hybrid formulas mix discrete and continuous variables. Engine 2 handles them
with projection-based approximate counting (PACT): it counts the satisfying
assignments to the discrete (bit-vector / Boolean) projection variables, while
the continuous part is discharged by the SMT solver.

This engine is auto-selected for non-``BV``, non-``LRA`` logics that have
bit-vector or Boolean projection variables. In the example below the projection
variables ``projA`` and ``projB`` are Boolean abstractions of constraints over
the real variable ``x`` and the integer variable ``y``:

.. code-block:: smtlib

   (set-logic QF_LIRA)
   (declare-fun x () Real)
   (declare-fun y () Int)
   (declare-fun projA () Bool)
   (declare-fun projB () Bool)
   (assert (and (>= x 0) (<= x 1)))
   (assert (and (>= y 0) (<= y 1)))
   (assert (= projA (>= x 0.5)))
   (assert (= projB (= y 0)))
   (check-sat)

Options
-------

``-P`` / ``--pact``
   Force projection-based approximate counting.

``-E`` / ``--enum``
   Enumerate the projected assignments exactly instead of approximately.

``--xor`` / ``--hash``
   Select the hashing backend and hash family used for approximate counting.
   See ``./ttc --help`` for the full list of backends.
