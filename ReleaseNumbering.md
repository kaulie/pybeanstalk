#summary How official releases are numbered

## Introduction ##

Keith Rarick, who is the lead for beanstalkd and beanstalk proto development, has stated that the protocol is likely to change until 1.0.  If this is the case, then this client will
likely change just as much, tracking the changes to the protocol.  To keep confusion minimal, the version numbering of the client will be numbered the same as the server.

The versions will follow a Major.Minor.Release-extra pattern, with major and minor being
those of the latest beanstalkd server this client can communicate with.

e.g. -- beanstalkd version 0.9 is corellated with pybeanstalk 0.9.0