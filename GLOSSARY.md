# Orientation glossary

The examples below use a cart that moves left or right to balance a hinged pole.

**Agent** — The decision-maker. In cart-pole, it selects how to move the cart.

**Environment** — Everything the agent interacts with: the cart, pole, physics, task rules, and episode logic.

**State** — A complete description of the environment at one moment, such as every relevant position and velocity.

**Observation** — The information given to the agent. It may contain the full state or only part of it.

**Action** — A choice the agent sends to the environment, such as a left/right command or a continuous force on the cart.

**Reward** — A number returned after a step that signals immediate progress toward the task.

**Return** — The accumulated rewards used to judge longer-term behavior, often with future rewards discounted.

**Policy** — The rule or learned model that maps an observation to an action or a distribution over actions.

**Value function** — An estimate of the return expected from a state, or from taking an action in a state.

**Trajectory (rollout)** — A sequence of observations or states, actions, and rewards produced through interaction.

**Episode** — One bounded run of the task: for example, from a cart-pole reset until it falls or reaches a time limit.

**Termination** — An episode ending because the task reached a defined terminal condition, such as the pole falling too far.

**Truncation** — An episode ending because of an outside limit, such as the maximum number of steps, rather than a terminal task state.
