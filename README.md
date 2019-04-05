# Artificial-Intelligence
Repository for Artificial Intelligence Lab


problems:


1  Motivation

The notions of agents and environments are key in AI and be specified as follows:
• An agent interacts with the environment (informaly surroundings) by performing actions.
The agent can also perceive (informally sense) the environment. In general, an agent is
expected to choose its actions based on what it perceives/senses.
• The environment is described by its state (informatlly status/configuration), and it responds
to the action of an agent by changing its state.
Please do look at https://github.com/aimacode/aima-python/ for example implementation of agents
and environments.

We will look at the some simple examples of agent-environment interaction.

2:Bunny needs help
Bunny is drifting in the middle of the ocean, and it does not know the location of the shore. Assume
that the world is 1-dimensional (shore could be left or right of the bunny), and come up a python
implementation of a) environment and b) wise-bunny agent which reaches shore. In order to complete
a) and b) you have to identify states, precepts, actions and the wise-bunny’s strategy.
What happens if the world is 2-dimensional? How will you modify?


3
Vaccum Robot
Imagine a 2-dimensional world with each location described as l = (x, y), where x, y are integers.
There is dirt in a location l d = (x d , y d ) and the vaccum robot has to start from location l s = (x s , y s ).
Come up a python implementation of a) environment b) wise-vr agent which picks the dirt.
The following example is to illustrate the importance of states internal to agents.


1    Motivation
Knowing the
right
decision is key. In this session, we will look at how
curse-of-dimensionality
makes
decision making diffcult. To understand the difficulty, we will make
random
decisions, and study its
effect as dimensions increase. Let us create the following three environments (in below
S
stands for
state-space and
A
for action-space)
•
Line
environment whose state space is given by
S
1
−
d
=
{
0
,
1
, . . . , L
−
1
, L
}
, the agent
starts at
s
0
=
d
L
2
e
. There are
2
actions namely move left by one step and move right by one
step.
•
2
-d Grid
environment has state space given by
S
2
−
d
=
S
1
−
d
×
S
1
−
d
, the agent starts at
s
0
= (
d
L
2
e
,
d
L
2
e
)
. There are
4
actions namely move up, down, right, left by one step.
•
Generalize the above to a
3
-d Grid
environment. The agent again starts at the center, and
the agent has
8
actions (why?).
•
Implement  a  random  agent  which  performs  a  random  action  at  any  given  state.   Use
numpy.rand.randint
to generate random actions.
•
The agent never leaves the grid, for illegal moves the agent stays in the same position.
•
In all the evnironment the reward is
0
for all the states except for the goal state
s
=
(
s
(1)
, s
(2)
, s
(3))
, such that
∑
d
i
=1
s
(
i
) =
dL
, where
d
is the dimension of the problem (this
is the goal state). The reward at the goal state sis
1
.
•
The aim of the random agent is to reach the goal state.
•
Measure the time it takes reach the goal in each of the cases. Try for cases
L
= 2
,
3
,
4
. Is
there any realtion to
|
A
|
|
S
|
?

1
(
n
2
−
1)
-puzzle
Implement the
(
n
2
−
1)
-puzzle environment. Also, implement parity function using the following
definition:
•
A position
p
i
is said to occur after
p
j
, if
p
i
occurs to the right of
p
j
in the same row or if
p
i
occurs at any row below
p
j
. This defines the ordering.
•
For a state
s
, let
d
(
s
)
denote the number of rows + number of columns that the empty square
is away from the bottom right corner.
•
Let
I
True
= 1
and
I
False
= 0
(this is known as
indicator
function).
•
For a state
s
, parity is given by
mod
(
d
(
s
) +
∑
p
i
,p
j
>p
i
I
p
j
(
s
)
<p
i
(
s
)
,
2)
, where
p
i
(
s
)
is the
number at the
i
th
position.
•
mod
(
n,
2)
is equal to the remainder on dividing
n
by
2
.
•
Imagine the empty square to be
n
2
.
2    Robot Navigation
Create the following navigation environment with blockades. Take
G
= 100
(grid-size), the blocked
places can be
0
’s and the other ones can be represented by
1
. The figure is only illustrative, and in a
grid blocking would mean blocking the entire cell.
