A pure python client library for putting and getting jobs from the beanstalkd queue.

More info about beanstalk can be found at the [project's homepage](http://xph.us/software/beanstalkd/)

**Feedback**: Please let us know if you find any problems, or have any suggestions for improvement.  Also, there are the beginnings of a twisted client in trunk right now. Give it a try!

**Latest**: 0.11.0 -- this version of the beanstalk client will work with beanstalkd 0.10 and 0.11.  beanstalkd is currently in a rc cycle for 1.0, which means that this client will work for most releases through 1.0.

Older versions are available on the download page.

**Important Note**: pybeanstalk is written to python 2.5  It takes advantage of some features that are new in that python version (specifically: the functools module, and generators that have the notion of .send()).  I am willing to help port this to older python versions, but am not going to do so unless someone will actually use that functionality. Feel free to contact me about such a change.

**Helping**: Anyone who wants to help out with this project is of course welcome to do so in the form of code, documentation, bug reports, and any other way. See the [Contributing](Contributing.md) page in the wiki, or contact me.