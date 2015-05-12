
SoundCloud Challenge Response
=============================

Iterative MapReduce solution using Python and Hadoop Streaming. Calculates connected friends (up to degrees specified) from given friend pairs.

Setup Instructions
==================
---

###1. Clone project

###2. Create and activate [virtualenv](http://www.virtualenv.org/en/latest/)
	virtualenv /path/to/my-project-venv
	source /path/to/my-project-venv/bin/activate

###3. Build project
	cd /path/to/datachallenge
	python setup.py install

###4. Run tests
	python tests/mapper_test.py
	python tests/reducer_test.py

###5. Run job locally
	bash runJobLocal.sh </path/to/data.tsv> <num_iterations>
	bash runJobLocal.sh data/sample.tsv 2

Bonus
=====
---
## Correctness

####First Iteration Map Step

The mapper initially generates all first degree connections from the input pairs (forward and backward).

#####First Iteration Sort Step

The sort step ensures that key value pairs are sorted lexicographically by key.

#####First Iteration Reduce Step

The reducer, for each incoming key, combines all first degree connections into a list. A secondary sort using the SortedSet guarantees lexicographical sorting of values

#####Subsequent Map Step

The next degree connections are generated for all pair permutations emitted from the previous reduce step compaction. We know all permutations from a line are at most +1 degree away because each member was previously a first degree connection with the leftmost person

#####Subsequent Iteration Sort Step

The sort step ensures that key value pairs are again sorted lexicographically by key.

#####Subsequent Reduce Step

The reducer again combines these connections. We know that they can only contain up to the next degree of friendships. The secondary sort again guarantees sort order of values.


## Complexity

The overall complexity approaches O(num_lines * num_names^2)

The name permutations contribute the n^2, and this logic operates for each line. The reducer is the same complexity as it operates on each pair once.