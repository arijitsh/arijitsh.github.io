Syntax
======

ttc reads standard `SMT-LIB 2 <https://smt-lib.org>`_ files. Counting is always
performed over a set of *projection variables*: ttc reports the number of
distinct assignments to those variables that can be extended to a model of the
formula.

Projection variables
---------------------

There are two ways to mark a variable for projection.

- **By prefix.** Any Boolean variable whose name starts with ``proj_`` is
  treated as a projection variable automatically.
- **By declaration.** Use the ``declare-projvar`` command to mark already
  declared variables explicitly.

.. code-block:: smtlib

   (declare-projvar x y)

When a formula mixes theories and a subset of the variables are bit-vector or
Boolean, ttc projects onto those by default. For a pure ``QF_LRA`` formula,
pass ``-P`` to project onto the Boolean variables instead.

Weighted counting
------------------

Use ``declare-weight`` to assign a weight to a Boolean literal. The weighted
count sums the weights of the satisfying assignments instead of counting them.

.. code-block:: smtlib

   (declare-weight x 0.1)

Weighted counting is currently supported only with exact enumeration (``-E``).

Example
-------

.. code-block:: smtlib

   (set-logic QF_UFBV)
   (declare-const x (_ BitVec 8))
   (declare-const y (_ BitVec 8))
   (declare-projvar x)
   (declare-weight x 0.1)
   (assert (= x #x0a))
   (check-sat)
