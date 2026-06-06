Hybrid Formulas
================

By hybrid formulas, we refer to formulas that contain both discrete and continuous variables. For example, the following formula is a hybrid formula:

.. code-block:: scheme

   (set-logic QF_UFBV)

   (declare-fun f ((_ BitVec 8)) (_ BitVec 8))
   (declare-const x (_ BitVec 8))

   (assert (= (f x) #x0a))
   (check-sat)