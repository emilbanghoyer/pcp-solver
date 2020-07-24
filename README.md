# pcp-solver
A small solver for the [Post's Correspondence Problem](https://en.wikipedia.org/wiki/Post_correspondence_problem) implemented in python.

This is an attempt to create a tool that enables us to solve some instances of the otherwise undecidable *Post's Correspondence Problem*.
The algorithm used in this program is a "brute-force" approach that runs *n* iterations (where *n* is a number specified by the user).
This means that the program will not be able to find the right answer to all inputs.
Sometimes more iterations of the program will be needed to find a solution (Who knows? The problem is undecidable).

This is a python implementation of the algorithm and pseudo code provided from [this website](https://www.arnevogel.com/post-correspondence-problem/).

More information about this approach to solving instances of PCP can be found in [this paper](https://webdocs.cs.ualberta.ca/~games/PCP/thesis/pcp.pdf).
