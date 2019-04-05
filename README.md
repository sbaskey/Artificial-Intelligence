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
