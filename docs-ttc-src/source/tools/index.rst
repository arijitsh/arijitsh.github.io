Set of Tools
============

ttc bundles four counting engines. Each targets a different fragment of SMT,
and the right engine is normally selected automatically from the logic and the
projection variables.

Basic usage
-----------

.. code-block:: bash

   ./ttc path/to/formula.smt2

The model count is printed on a line of the form:

.. code-block:: text

   s mc 42

Pass ``-a`` for approximate counting (tune the guarantee with ``--epsilon`` and
``--delta``), and ``-v`` to control verbosity.

The four engines
----------------

.. list-table::
   :header-rows: 1
   :widths: 8 30 25

   * - Engine
     - Task
     - Auto-selected for
   * - 1
     - :doc:`Bit-vector counting <../bitvectors/index>`
     - ``BV`` / ``UFBV`` logics
   * - 2
     - Projection counting (``-P``)
     - other theories with BV/Bool projection vars
   * - 3
     - :doc:`LRA volume computation <../volume/index>`
     - ``QF_LRA`` with no projection vars
   * - 4
     - :doc:`Function counting <../function/index>` (``--skolemfc``)
     - uninterpreted-function counting

Automatic engine selection
---------------------------

When no engine is forced, ttc picks one as follows:

1. logic ``BV`` / ``UFBV`` → bit-vector ApproxMC (eager bit-blast)
2. other theories with BV/Bool projection variables → projection counting
3. ``QF_LRA`` with no projection variables → LRA volume computation
4. otherwise → unsupported (reports an error and exits)

Any engine can be forced explicitly with its flag (for example ``-P``,
``--skolemfc``, or ``--bvcnf``).
