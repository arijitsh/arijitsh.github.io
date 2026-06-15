Counting on Bitvectors
======================

Engine 1 counts the models of formulas over the theory of fixed-size
bit-vectors (logics ``BV`` and ``UFBV``). The formula is eagerly bit-blasted to
a model-preserving CNF in memory and counted with Arjun + ApproxMC in-process,
so no intermediate file is written. This engine is auto-selected for bit-vector
logics.

.. code-block:: smtlib

   (set-logic QF_UFBV)

   (declare-fun f ((_ BitVec 8)) (_ BitVec 8))
   (declare-const x (_ BitVec 8))

   (assert (= (f x) #x0a))
   (check-sat)

Options
-------

``--bvcnf``
   Force engine 1 (auto-selected for ``BV`` / ``UFBV`` logics).

``--cnf``
   Also write the bit-blasted, model-preserving CNF to ``<input>.cnf`` in
   DIMACS form. The count is still produced in-process.

For approximate counting, combine with ``-a`` and tune ``--epsilon`` /
``--delta``.
