# CartPole report

Replace each TODO with your own observations. Keep this report short; link code,
compact results, and images instead of pasting logs.

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

## Model and task

TODO: Link a small model screenshot (`../results/model.png`). Explain the XML include,
slide/hinge axes, unactuated pole, box half-extents, and degrees versus radians.

Describe the task supplied by Gymnasium in your own words. For each row, identify
the method, attribute, or XML setting you inspected to understand its behavior.

| Component                              | Your explanation of the supplied task |
| -------------------------------------- | ------------------------------------- |
| Observation order, shape, dtype, units | TODO                                  |
| Action range and gear                  | TODO                                  |
| Physics/control timing                 | TODO                                  |
| Reset and seeding                      | TODO                                  |
| Reward                                 | TODO                                  |
| Termination                            | TODO                                  |
| Truncation                             | TODO                                  |

TODO: Follow reset and one step in the supplied source code. Identify where MuJoCo
stores `qpos`, `qvel`, and `ctrl`, and explain how the environment builds its
observation and computes the reward. Use the linked documentation for reference;
you do not need to write code to access these values. Distinguish
falling from the time limit, and joint travel limits from episode endings. Name
one bug caught by a behavior test, and explain the SB3 action-range warning.

## Training

- Run name / source commit / training seed: TODO
- Requested and actual steps / elapsed time / device: TODO
- Configuration and versions: TODO link `../results/<run>/run.json`
- Learning curve: TODO embed `../results/<run>/learning-curve.png`

TODO: Explain the curve's axes, averaging and smoothing, and whether learning
improved. What do SB3, PyTorch, and Monitor each do here?

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

TODO: Explain why this evaluation differs from a training curve, and what one
trained seed cannot establish. What carries over to humanoid soccer, and what is
missing (for example, contacts, partial observations, or sim-to-real transfer)?

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
