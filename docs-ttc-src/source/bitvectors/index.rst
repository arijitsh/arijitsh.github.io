Counting on Bitvectors
====================

The first engine counts on bitvectors.


.. code-block:: scheme

   (set-logic QF_UFBV)

   (declare-fun f ((_ BitVec 8)) (_ BitVec 8))
   (declare-const x (_ BitVec 8))

   (assert (= (f x) #x0a))
   (check-sat)