# Cart-pole onboarding

**Status: preview.** Detailed setup, starter files, rubric, and submission instructions are forthcoming. Nothing on this page is required before the orientation meeting.

The first assignment will be a guided, end-to-end RL experiment: model a cart-pole in MuJoCo, expose it through Gymnasium, train a PPO policy with Stable-Baselines3, inspect training in TensorBoard, and evaluate the saved policy separately.

## What you will learn

- How a physical model differs from an RL task
- How observations, continuous actions, rewards, resets, termination, and truncation fit together
- How to validate an environment before training
- How to train, save, reload, and evaluate a policy
- How to report a small experiment without overclaiming its result

## Expected schedule

Plan for **8–12 focused hours over two weeks**, with a third week available as a buffer.

- **End of week one:** the environment installs; the model loads and renders; random actions run; spaces and episode endings are documented; environment checks pass.
- **End of week two:** PPO trains; the policy saves and reloads; TensorBoard curves and a separate multi-episode evaluation are complete; one rollout and a short report are ready.

## Model structure

The starter will keep the reusable mechanism separate from its surroundings:

```text
assets/
├── cartpole.xml  # cart, pole, joints, geometry, and actuator
└── scene.xml     # floor, lighting, camera, and included model
```

This small example practices the model-plus-scene composition we will later use with larger robots. The canonical instructions will live here; member solutions and future robot-specific work will live in separate repositories.
