# CartPole report

Replace each TODO with your own observations. Keep this report short; link code,
compact results, and images instead of pasting logs.
For each stage, explain which tool or function uses your inputs, where the
results come from, and what uses them next. Point to the relevant code or
documentation; a few sentences or an annotated arrow diagram is enough.

To link a file in Markdown, use `[link text](relative/path/to/file)`.
For example, `[Environment code](../onboarding/env.py)` becomes
[Environment code](../onboarding/env.py). Links are relative to this report's
`docs/` folder; use `../` to reach the repository root.
To display an image, add `!`: `![Model screenshot](../results/model.png)`.

## Setup

- Member: TODO
- OS: TODO
- Setup diagnostic, viewer, and RGB results; any fix needed: TODO
- Fork URL and working branch: TODO
- Before starting, read the [toolchain overview](../resources/toolchain.md).
  What role does each of MuJoCo, Gymnasium, Stable-Baselines3, and TensorBoard
  play in this exercise? Describe how they work together in your own words: TODO

## Model and task

### Model (Stage 2)

- Which tool loads `scene.xml` and its included `cartpole.xml`, and what does it
  create from them? Point to the loading call in `scripts/view_model.py`. Which
  tool computes the motion you see in the viewer when a control is applied? TODO
- Which XML file owns the mechanism, and how does the include connect it to the
  scene? Explain the slide/hinge axes, unactuated pole, box half-extents, and
  degrees versus radians. Link a small model screenshot (`../results/model.png`): TODO

### Environment (Stage 3)

Describe the task supplied by Gymnasium in your own words. For each row, identify
the method, attribute, or XML setting you inspected to understand its behavior,
including which part comes from MuJoCo and which Gymnasium defines.

| Component                              | Your explanation of the supplied task |
| -------------------------------------- | ------------------------------------- |
| Observation order, shape, dtype, units | TODO                                  |
| Action range and gear                  | TODO                                  |
| Physics/control timing                 | TODO                                  |
| Reset and seeding                      | TODO                                  |
| Reward                                 | TODO                                  |
| Termination                            | TODO                                  |
| Truncation                             | TODO                                  |

Use the supplied source and documentation to answer these questions; you do not
need to write code to access the simulation state.

- How does the `xml_file` input you pass to `gym.make()` reach the simulator?
  What does Gymnasium add around that model to make it an RL task? TODO
- Follow `reset()` and one `step(action)`: where are `qpos`, `qvel`, and `ctrl`
  stored? Who initializes the state, who advances the physics, and how does
  `_get_obs()` build an observation from that state? During policy training,
  what uses the returned observation to choose the next action, and how does
  that action reach the motor? TODO
- Which code computes the reward and each ending flag? Distinguish falling from
  the time limit, and joint travel limits from episode endings: TODO
- What bug did a behavior test catch, and what does the SB3 action-range warning
  mean? TODO

## Training

- Run name / source commit / training seed: TODO
- Requested and actual steps / elapsed time / device: TODO
- Configuration and versions: TODO link `../results/<run>/run.json`
- Learning curve: TODO embed `../results/<run>/learning-curve.png`

- What do SB3, PyTorch, and `Monitor` each do here? How does SB3 use the environment
  and settings you pass to PPO, and what produces the saved `policy.zip`? TODO
- What do the curve's axes, averaging, and smoothing mean, and what evidence of
  improvement, variability, or a plateau do you see? TODO

## Evaluation

Use reset seeds 10000–10019, deterministic PPO actions, and random action seeds
`reset seed + 20000`. Standard deviations describe episodes (`ddof=0`).

| Agent | Episodes | Return mean ± std | Length mean ± std | Time-limit fraction |
| --- | --- | --- | --- | --- |
| Random | TODO | TODO | TODO | TODO |
| PPO | TODO | TODO | TODO | TODO |

- Per-episode CSV and summary JSON: TODO links
- Predetermined PPO rollout (seed 10000): TODO briefly describe the behavior you observed
- Limitation or failure, and a specific diagnosis if learning was weak: TODO

- How does `onboarding/evaluate.py` use `policy.zip` and fresh environment
  observations to choose actions? How are random-baseline actions chosen, and
  does either evaluation update the policy? TODO
- Where do the returns, lengths, and ending flags in `episodes.csv` come from,
  and how does `summary.json` summarize them? Trace the video from simulation
  state through `env.render()` to the encoder. Does the policy act on the
  numerical observation vector or the rendered frames in this exercise? TODO
- Why does this evaluation differ from a training curve, and what can one
  trained seed not establish? What carries over to humanoid soccer, and what is
  missing (for example, contacts, partial observations, or sim-to-real transfer)? TODO

## Reproduce and review

TODO: Record exact setup, test, train, and evaluate commands, plus any rendering
environment variable.

Keep the saved policy, TensorBoard logs, and rollout video locally and share them
directly with the RL lead if requested. No file uploads, download links, or GitHub
release are required for these files.

- Automated test results: TODO
- Manual model/render/video checks: TODO
- Fork PR link and review notes (record merge in the PR): TODO

## Feedback

- Did you learn anything from this onboarding? What was new, or what became
  clearer? If little was new, say so: TODO
- What improvements would make the onboarding easier to follow or more useful?
  Mention any confusing instructions, missing background, or unnecessary work: TODO
