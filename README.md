# Phylo-HMGP
Continuous-trait Phylogenetic Hidden Markov Gaussian Process Model

Part of the code is developed based on modification or reusing the source code of the hmmlearn package https://github.com/hmmlearn/hmmlearn.

The source code base1.py is developed based on modification of the file base.py from the hmmlearn package. The source code utils.py and _hmmc.c are reused from the hmmlearn package. Some functions in phylo_hmgp.py are used with modifications from the functions in the file hmm.py from the hmmlearn package. 

A statement on reusing the source code of the hmmlearn package, by the requirement of the copyright holders of hmmlearn, is available in the file folder statement_hmmlearn. A list of the authors of the hmmlearn package, as complementary to the statement, is also included in the file folder statement_hmmlearn.

The command to use Phylp-HMGP for evolutionary state estimation is as follows. 

python phylo_hmgp.py [Options]

- -n, --num_states : the number of states to estimate for Phylo-HMGP, default = 10

- -p, --root_path : root directory of the data files

- -r, --run_id : experiment id, default = 0

- -c, --cons_param : constraint parameter, default = 1

- -t, --method_mode : method_mode: 0- Phylo-HMGP-BM; 1- Phylo-HMGP-OU, default = 1

- -i, --initial_weight : initial weight for initial parameters, default = 0.1

- -j, --initial_magnitude : initial magnitude for initial parameters, default = 2

- -s, --version : dataset version, default = 1

Example: python phylo_hmgp.py -t 0 -n 20 -r 0 (using Phylo-HMGP-OU for estimating 20 states on the provided example data)

To use Phylo-HMGP, please first complie the C source file _hmmc.c into a Python module named _hmmc. The module _hmmc is needed and imported in the file _base1.py. A sample setup.py is provided. Please use the following commands to compile the _hmmc module:

python setup.py build

python setup.py install

************************************************************************************
# Required pre-installed packages
Phylo-HMGP requires the following packages to be installed:
- Python (tested on version 2.7.12)
- scikit-learn (tested on version 0.18.1)
- NumPy (tested on version 1.13.1)
- SciPy (tested on version 0.19.0)

You could install the Anaconda (avilable from https://www.continuum.io/downloads) for convenience, which provides a open souce collection of widely used data science packages including Python and numpy. PEP is tested using Anaconda 4.1.1.

