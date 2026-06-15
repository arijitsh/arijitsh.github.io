Installation
============

ttc is a C++ tool. The instructions below build it from source on Linux.

Required packages
-----------------

The following system packages are needed to configure and build ttc:

.. code-block:: bash

   sudo apt install build-essential cmake git \
       libboost-program-options-dev \
       libgmp-dev \
       libeigen3-dev \
       libisl-dev \
       libcdd-dev \
       liblpsolve55-dev

These provide the build toolchain plus the libraries ttc links against:
Boost ``program_options`` (command-line parsing), GMP (exact arithmetic),
Eigen3 and ISL (the volume engine), cddlib (polytope canonicalization), and
lp_solve (linear programming).

Optional packages
------------------

These are linked when present and otherwise skipped:

- ``libsuitesparse-dev`` — COLAMD / AMD sparse-matrix routines.
- ``libstp-dev`` — the STP bit-vector solver backend.

Bundled solver components
-------------------------

A few backends are built from source rather than installed as packages, and
``configure.sh`` wires them in:

- a modified version of `cvc5 <https://github.com/meelgroup/ttc>`_ (the core
  SMT engine);
- a patched CaDiCaL build (the XOR engine used by projection counting);
- the SkolemFC stack, which enables the ``--skolemfc`` function-counting
  engine.

Building from source
--------------------

.. code-block:: bash

   git clone https://github.com/meelgroup/ttc
   cd ttc
   ./configure.sh
   cd build && make -j8

Run ``./configure.sh -h`` for other build options (``--local``, ``--static``,
``--debug``, ``--ddnnf``) and for instructions on building on macOS. The
resulting binary is ``build/ttc``.
