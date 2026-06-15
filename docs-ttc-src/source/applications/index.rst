Applications
============

Many quantitative reasoning problems reduce to counting the models of an SMT
formula. This page collects applications that ship as examples with ttc.

Probabilistic Model Checking
----------------------------

Reachability probabilities in a probabilistic model can be expressed as a
weighted count over the paths of the model. Encode the model and its paths as
an SMT formula, mark the path variables for projection, and let ttc count them
(see the ``jani-examples`` benchmarks under ``example/applications``).

Network Reliability
-------------------

The reliability of a network — the probability that a source stays connected to
a sink when links fail independently — is a weighted model count over the
configurations of working and failed links. Each link becomes a Boolean
variable; ttc counts the configurations that keep the network connected (see
the ``node*_edge*`` benchmarks under ``example/applications``).
