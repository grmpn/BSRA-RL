# CartPole report

Replace each TODO with your own observations. Keep this report short; link code,
compact results, and artifacts instead of pasting logs.

## Setup

- Member: TODO
- OS / architecture; Python and uv versions: TODO
- Setup diagnostic, viewer, and RGB results; any fix needed: TODO
- Fork URL and working branch: TODO

## Model and task

TODO: Link a small model screenshot (`results/model.png`). Explain the XML include,
slide/hinge axes, unactuated pole, box half-extents, and degrees versus radians.

| Component | Your task definition |
| --- | --- |
| Observation order, shape, dtype, units | TODO |
| Action range and gear | TODO |
| Physics/control timing | TODO |
| Reset and seeding | TODO |
| Reward | TODO |
| Termination | TODO |
| Truncation | TODO |

TODO: Trace reset and one step. Distinguish state from observation, falling from
the time limit, and joint travel limits from episode endings. Name one bug caught
by a behavior test, and explain the SB3 action-range warning.

## Training

- Run name / source commit / training seed: TODO
- Requested and actual steps / elapsed time / device: TODO
- Configuration and versions: TODO link `results/<run>/run.json`
- Learning curve: TODO embed `results/<run>/learning-curve.png`

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
- Predetermined PPO video (seed 10000): TODO artifact link
- Limitation or failure, and a specific diagnosis if learning was weak: TODO

TODO: Explain why this evaluation differs from a training curve, and what one
trained seed cannot establish. What carries over to humanoid soccer, and what is
missing (for example, contacts, partial observations, or sim-to-real transfer)?

## Reproduce and review

TODO: Record exact setup, test, train, and evaluate commands, plus any rendering
environment variable. Link your fork's `cartpole-v1` release containing the policy,
video, and logs. Include where to place the downloaded policy.

- Automated test results: TODO
- Manual model/render/video checks: TODO
- Fork PR link and review notes (record merge in the PR): TODO
