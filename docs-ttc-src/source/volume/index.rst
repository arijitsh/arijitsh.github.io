Volume Computation
==================

Engine 3 computes the volume of the solution space of linear real arithmetic
(``QF_LRA``) formulas — that is, the measure of the region of real assignments
that satisfy the formula. The polytopes are estimated with the volesti
random-walk sampler. This engine is auto-selected for ``QF_LRA`` inputs with no
projection variables.

The formula may combine several regions through Boolean structure; the volume
of their union is reported:

.. code-block:: smtlib

   (set-logic QF_LRA)
   (declare-fun a () Bool)
   (declare-fun b () Bool)
   (declare-fun x () Real)
   (declare-fun y () Real)

   (assert (or a b))
   (assert (=> a (and (> x 10) (< x 35) (> y 10) (< y 35))))
   (assert (=> b (and (> x 15) (< x 40) (> y 15) (< y 40))))

   (check-sat)

Options
-------

``--walklen-vol`` / ``--walklen-samp``
   Random-walk length for the volume estimator and for point sampling.

``--no-cdd-simp``
   Skip cddlib polytope canonicalization (redundant-constraint removal) before
   volume estimation.

``--nogmp`` / ``--fullgmp`` / ``--precision``
   Control the numeric precision of sampling and membership tests. By default
   ttc works in GMP at a precision derived from the polytopes.
