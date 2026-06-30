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

The SAT, counting, and SMT back-ends are built from source rather than
installed as packages, and ``configure.sh`` links them in. You do not install
these with ``apt``; they come from the companion meelgroup repositories.

The core SMT layer is a modified version of `cvc5
<https://github.com/meelgroup/ttc>`_, together with the libraries it bundles:

- **poly** (``picpoly`` / ``picpolyxx``) — polynomial arithmetic;
- **CaDiCaL** — a hand-patched build whose XOR engine drives projection
  counting;
- **CryptoMiniSat** — the bit-vector SAT back-end.

The counting and sampling stack comes from the
`SkolemFC <https://github.com/meelgroup/skolemfc>`_ build and supplies the
approximate-counting machinery used by the bit-vector and function-counting
engines:

- **ApproxMC** (``approxmc``) — approximate model counter;
- **Arjun** (``arjun``) — independent-support / preprocessing front-end;
- **UniGen** (``unigen``) — uniform sampler;
- **CryptoMiniSat** (``cryptominisat5``) — the underlying SAT solver;
- **SBVA** (``sbva``), **Louvain-Communities** (``louvain_communities``),
  **CaDiCaL** / **CaDiBack** — additional archives pulled in for fully static
  (``--static``) builds.

The standard math libraries ``m``, ``dl``, ``gmp`` and ``gmpxx`` are linked as
well.

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
