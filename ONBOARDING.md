# CartPole onboarding

Build a MuJoCo cart-pole, connect it to Gymnasium, and train and evaluate a PPO
policy. Finish with a short report and a pull request in your own fork.
This is a learning exercise; robot skills and larger experiments belong in separate repositories.

Start after the [orientation](ORIENTATION.md). You need basic Python functions,
classes, and imports; Git and RL experience are not required. Budget about
**8–12 focused hours over two weeks**, with a third week for setup or debugging.
The effort estimate still needs a beginner pilot.

| Section | Outcome | Time |
| --- | --- | --- |
| 1. Setup | Working fork, branch, and Python environment | 1.5–2 h |
| 2. Model | Two composed XML files that load and move | 2–3 h |
| 3. Environment | A checked, documented RL task | 1.5–2 h |
| 4. Training | Saved policy and TensorBoard logs | 1–2 h |
| 5. Evaluation | Baseline comparison and one recorded episode | 1–1.5 h |
| 6. Handoff | Report and reviewed, merged fork PR | 1–1.5 h |

**Member files:** complete `MEMBER TODO` blocks in `assets/cartpole.xml`,
`assets/scene.xml`, `onboarding/env.py`, `onboarding/train.py`, and
`onboarding/evaluate.py`; fill in [REPORT.md](REPORT.md).
`scripts/` contains commands you run; `onboarding/` contains the Python you edit.
The supplied `test/` checks describe the assignment contract. Tests for unfinished
sections are expected to fail; the setup diagnostic works immediately.

**Review status:** the starter is developed on `onboarding`; the completed example
is on `onboarding-validation`. The fork instructions below assume the starter has
been merged into the hub's `main` before a cohort starts. To review locally now,
use either branch directly and start at `uv sync`.

## 1. Setup and Git workflow

Read the [toolchain overview](resources/toolchain.md). Install
[Git](https://docs.github.com/en/get-started/git-basics/set-up-git) and
[uv](https://docs.astral.sh/uv/getting-started/installation/) in the environment
where you will run the exercise. New to terminals? Read the
[Ubuntu command-line introduction](https://ubuntu.com/tutorials/command-line-for-beginners)
through working with directories. `pwd` shows your directory; `cd` changes it.

| Platform | Setup |
| --- | --- |
| Windows | Use **WSL2 with Ubuntu**. Follow [Microsoft's setup guide](https://learn.microsoft.com/en-us/windows/wsl/setup/environment), then check `wsl -l -v` in PowerShell. Run all assignment commands inside Ubuntu. Keep the clone under a Linux path such as `~/dev/BSRA-RL`. Check [WSLg](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps) before the viewer step. |
| Linux x86-64 | Use the native terminal and CPU dependencies supplied here. |
| Apple Silicon macOS | Use native ARM64 Python through uv. CPU training is configured. Use the `mjpython` viewer commands below. This platform still needs a runtime pilot of this lockfile. |
| Intel Mac / other architectures | This lockfile does not target these systems. Arrange access to a Linux x86-64 machine with a maintainer before starting. |

The dependency set uses Python 3.12.3 and was installed with uv 0.12.13 on Ubuntu
under WSL2 x86-64. Training, WSLg viewing, and software offscreen rendering are checked there;
that does not establish compatibility or runtime on every laptop.

### Fork, clone, and install

Follow [GitHub's fork guide](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo)
to fork [grmpn/BSRA-RL](https://github.com/grmpn/BSRA-RL) into your account.
A **fork** is your GitHub repository; a **clone** is its local copy.
Configure your [Git name](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git),
[email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address),
and authentication using the Git setup guide above. Replace `YOUR-USERNAME`:

```bash
git clone https://github.com/YOUR-USERNAME/BSRA-RL.git
cd BSRA-RL
git remote -v
git switch -c onboarding/cartpole
git status
uv sync
uv run python scripts/check_setup.py
```

Check that `origin` points to **your fork**. Stay in `BSRA-RL/` for every command.
`uv sync` creates `.venv`, installs the dependencies recorded in `uv.lock`, and
installs the local package in editable mode. Your Python edits take effect without
reinstalling it. Select `.venv/bin/python` in your editor
([VS Code instructions](https://code.visualstudio.com/docs/python/environments)).
Use `uv run` to run commands inside that environment.

Leave `pyproject.toml`, `uv.lock`, and `.python-version` unchanged during the
assignment. Video encoding is included; no extra packages or CUDA setup are needed.
See [uv projects](https://docs.astral.sh/uv/guides/projects/) and
[lockfile behavior](https://docs.astral.sh/uv/concepts/projects/sync/).
If dependency files change unexpectedly, inspect the diff with a maintainer.

Check rendering separately:

```bash
uv run python scripts/check_setup.py --viewer
uv run python scripts/check_setup.py --rgb
```

On macOS, replace the first command with
`uv run mjpython scripts/check_setup.py --viewer`; ordinary training uses Python.
MuJoCo requires this launcher for its
[passive viewer](https://mujoco.readthedocs.io/en/stable/python.html#passive-viewer).

**Check:** package, CPU, encoder, and physics checks pass; a falling sphere appears
for three seconds and the window closes. The fixture is independent of your XML.
If a viewer fails, resolve the display/WSLg setup before working on the model.
On a headless Linux machine with OSMesa installed, use
`MUJOCO_GL=osmesa uv run python scripts/check_setup.py --rgb` for offscreen rendering;
this does not check an interactive window.

Add your OS, setup results, and any fixes to `REPORT.md`, then practice:

```bash
git status
git diff
git add REPORT.md
git commit -m "Record onboarding setup"
git push -u origin onboarding/cartpole
```

A commit saves a local revision; a push uploads it to your fork. Confirm the
commit appears on GitHub. Repeat this cycle after each section, staging the files
you edited. The final workflow is **branch → push → PR into your fork → review → merge**.

## 2. XML model and scene creation

**Before starting:** setup passes. Read MuJoCo's
[modeling introduction](https://mujoco.readthedocs.io/en/stable/modeling.html)
on bodies, joints, geoms, and actuators; use the
[XML reference](https://mujoco.readthedocs.io/en/stable/XMLreference.html) for attributes.

Sketch the cart, pole, slide axis, hinge axis, and motor. Then fill the two XML
files. `scene.xml` is the top-level `<mujoco>` model; its `<include>` inserts the
contents of `cartpole.xml`'s `<mujocoinclude>` root. Put the mechanism's
`<worldbody>` and `<actuator>` sections in that included file. The scene owns
global options, scenery, lighting, and a camera.

| Element / required name | Specification |
| --- | --- |
| Body `cart`, geom `cart_geom` | Body at `0 0 0.20`; box full dimensions `0.30 × 0.20 × 0.16 m`, mass `10 kg` |
| Body `pole`, geom `pole_geom` | Child of cart at `0 0 0.08`; capsule from `0 0 0` to `0 0 0.75`, radius `0.04 m`, mass `5 kg` |
| Joint `slider` | Slide along `1 0 0`, limited to `[-1.25, 1.25] m`, damping `1` |
| Joint `hinge` | Hinge along `0 1 0`, limited to `[-90, 90]` degrees, damping `1` |
| Motor `cart_motor` | Acts on `slider`, limited control `[-3, 3]`, gear `100` |
| Scene | Degree compiler units; gravity `0 0 -9.81`, RK4 integrator, timestep `0.02 s` |
| Scenery | Floor, rail, light, and camera named `side`; disable collisions for **all** geoms with `contype="0" conaffinity="0"` |

Box `size` values are **half-extents**. Capsule endpoint separation excludes its
rounded caps. With these placements, zero joint positions put the pole upright;
the hinge is unactuated. XML angles use degrees here, while runtime joint angles
use radians. Colors, camera placement, and scenery dimensions are your choice.

```bash
uv run python -m pytest test/test_model.py -q
uv run python scripts/view_model.py
uv run python scripts/view_model.py --control 0.1 --seconds 1
uv run python scripts/view_model.py --control -0.1 --seconds 1
```

On macOS use `uv run mjpython scripts/view_model.py ...`.
Each viewer trial starts from zero. Rotate the camera to check the axes.
**Check:** tests pass, opposite controls move the cart in opposite directions,
and the pole rotates about the hinge. It need not balance without a policy.
Save a small screenshot in `results/model.png`, link it in the report, and explain
which XML file owns the mechanism. Commit the two XML files and report evidence.

## 3. Environment definition and validation

**Before starting:** model tests pass. Review
[Gymnasium basic usage](https://gymnasium.farama.org/introduction/basic_usage/) and
the [InvertedPendulum task](https://gymnasium.farama.org/environments/mujoco/inverted_pendulum/).
We use its supplied behavior with our custom model, rather than writing a simulator
or environment class from scratch.

Complete `make_env()` in `onboarding/env.py`, using the supplied path and task
constants. Pass the rendering mode and episode limit through to `gym.make()`.
The latter applies the `TimeLimit` wrapper. Fill the task table in `REPORT.md`:

| Component | Required behavior |
| --- | --- |
| Observation | `qpos` followed by `qvel`: cart position (m), pole angle (rad), cart velocity (m/s), pole angular velocity (rad/s); unbounded `(4,)` float64 Box |
| Action | `(1,)` float32 Box, `[-3, 3]`; motor control, multiplied by gear `100` to produce cart force in N |
| Timing | Two `0.02 s` physics steps per action: `0.04 s`, or 25 actions/s |
| Reset | Upright zero state plus independent uniform `[-0.01, 0.01]` noise on each position and velocity, using Gymnasium's seeded RNG |
| Reward | `1` for a healthy state after the action, otherwise `0` |
| Termination | Any non-finite observation or absolute pole angle greater than `0.2 rad` |
| Truncation | At 1,000 environment steps |

The physical cart travel limit does not itself end an episode. Explain why falling
and reaching a time limit are different and why the rollout must reset after either.
Trace `reset()` and `step()` in the
[upstream implementation](https://github.com/Farama-Foundation/Gymnasium/blob/v1.2.3/gymnasium/envs/mujoco/inverted_pendulum_v5.py):
where does physics run, and where are observations and rewards made?

The supplied random-action path works before the evaluation TODOs are filled:

```bash
uv run python -m pytest test/test_env.py -q
uv run python scripts/evaluate.py --random-only --run-name random-debug --episodes 3 --trace
uv run python scripts/evaluate.py --random-only --run-name random-debug --episodes 3 --video
```

Open `videos/random-debug/episode-10000.mp4`. On headless Linux, prefix the video
command with `MUJOCO_GL=osmesa` if that renderer passed Setup.
`--trace` prints observations, actions, rewards, and ending flags.

**Check:** API and behavior tests pass; random episodes end and reset; the custom
scene is visible. SB3 warns that the action range is not normalized to `[-1, 1]`.
Keep `[-3, 3]` for this task and record that warning. Explain one bug that the
behavior tests catch beyond an API shape check.

## 4. Training and experiment tracking

**Before starting:** environment checks pass. Read the introduction and example in
[SB3's PPO guide](https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html).
PPO collects experience and updates a policy; SB3 handles the PyTorch network and
optimizer. You supply the environment and experiment settings.

Complete the three training TODOs in `onboarding/train.py`: construct PPO with
`MlpPolicy`, learn, and save. Use the provided monitored environment, seed, CPU
device, TensorBoard path, and `settings`. `Monitor` supplies episode return/length
statistics. The default settings are explicit in `PPO_SETTINGS`; keep them for
your first run. The supplied code writes versions, task hashes, source revision,
requested/actual steps, runtime, and output paths to `results/<run>/run.json`.

```bash
uv run python -m pytest test/test_pipeline.py -k training_smoke -q
uv run python scripts/train.py --run-name smoke --smoke
uv run python scripts/train.py --run-name first-run --seed 0 --steps 100000
uv run tensorboard --logdir runs
```

Open TensorBoard's printed local URL. Look at `rollout/ep_rew_mean` and
`rollout/ep_len_mean`. The horizontal axis is environment steps, not episodes;
each statistic averages up to the most recent 100 training episodes. Set UI
smoothing to zero for the report and save a small curve image at
`results/first-run/learning-curve.png`. Explain improvement, variability, or a plateau.

The smoke run is 256 steps and checks the pipeline, not learning. The full
100,000-step budget is a starting point, not a promised score. PPO collects full
rollouts, so with 2,048 steps per rollout it actually collects **100,352** steps.
Run names cannot be reused for training; choose a new name to preserve earlier work.

**Check:** the training test passes, `models/first-run/policy.zip` exists, and
TensorBoard has real episode statistics. Record elapsed time and settings. Commit
your code before the full run so its metadata points to a reproducible revision.

## 5. Evaluation and interpretation

**Before starting:** a saved policy and matching `run.json` exist. Complete the
two evaluation TODOs in `onboarding/evaluate.py`: load the policy on CPU and
predict deterministic actions. Evaluation runs in a fresh process and never learns.

```bash
uv run python -m pytest test/test_pipeline.py -q
uv run python scripts/evaluate.py --policy models/first-run/policy.zip --run-name first-run --video
```

Use the same run name as training. The command verifies the policy and task
against the training record, then compares PPO and random actions on reset seeds
**10000–10019**. Reserve these seeds for evaluation. Random action sampling has
its own seed (`reset seed + 20000`). Both agents get the same starting-state seeds.

`results/first-run/episodes.csv` records each return, length, seed, and ending flags.
`summary.json` contains means, population standard deviations (`ddof=0`), and the
fraction reaching the time limit. Repeating evaluation replaces these outputs;
it does not append episodes. Random-only debugging uses a separate run name.

`--video` records the **actual PPO episode with seed 10000**, selected in advance.
That episode is counted once in the results. The supplied encoder streams 640 × 480
frames into `videos/first-run/episode-10000.mp4` at 25 fps, derived from the control
interval. Other episodes run without rendering. Without `--video`, no encoder
starts and the new summary records no video.

**Check:** tests pass and the video plays. Compare the baseline and policy in the
report. A training curve and a good-looking video do not replace multi-episode
evaluation. These episodes measure varied starts for one trained policy, not
variation across training seeds. There is **no required return threshold**.
If learning is weak, use checks and logs to support one diagnosis; do not select
a better-looking video seed or hide failed episodes.

## 6. Report and GitHub handoff

Finish `REPORT.md`: setup, model/task explanation, reproduction commands, learning
curve, baseline comparison, selected rollout, and one limitation. Explain what
carries over to humanoid control and what this exercise leaves out.

```bash
uv run python -m pytest -q
git status
git diff
git add assets onboarding REPORT.md results
git diff --cached
git commit -m "Complete CartPole onboarding report"
git push
```

Commit compact JSON/CSV results and images. `.venv`, `models`, `runs`, and `videos`
are ignored. Put the policy, rollout video, and a ZIP of TensorBoard logs in a
[GitHub release in your own fork](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository),
tagged `cartpole-v1` at your solution commit. Link its assets in `REPORT.md`, then
commit and push the link update. A reviewer should download the policy to
`models/first-run/policy.zip`; the recorded hash checks that it is the right file.

Follow [GitHub's PR instructions](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request).
Inspect the repository selector: **base repository `YOUR-USERNAME/BSRA-RL`, base
branch `main`, compare branch `onboarding/cartpole`**. Member solutions stay in
member forks. Example description:

> Completes the custom CartPole model and PPO experiment. Report and artifacts:
> REPORT.md. Checks: setup, model/environment tests, smoke train, saved-policy
> evaluation, and playable seed-10000 video. Limitation: one training seed.

Review the diff, request a peer or mentor review where available, and address
feedback on the same branch. Record the review in the PR, then merge it through
GitHub. The merged fork PR is your handoff link; share it with the RL lead in
your existing team conversation.

```bash
git switch main
git pull --ff-only origin main
```

**Completion check:** a reviewer can clone your fork, run `uv sync` and the tests,
download the saved policy, and reproduce the evaluation with the report's command.
Full retraining is optional for review. The report, artifact links, and reviewed,
merged PR must all be present.

Official references checked 2026-09-20. Maintainers should pilot setup, interactive
rendering, and video on each cohort's platforms before assigning the exercise.
