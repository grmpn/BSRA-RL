"""Check installation before completing any member TODOs."""

import argparse
import importlib
from importlib.metadata import version
import platform

FIXTURE = """<mujoco><worldbody><body pos="0 0 1">
  <joint type="slide" axis="0 0 1"/>
  <geom type="sphere" size="0.1" mass="1"/>
</body><light pos="0 -1 3"/></worldbody></mujoco>"""


def check(label, function):
    try:
        function()
        print(f"PASS {label}")
        return True
    except Exception as error:
        print(f"FAIL {label}: {type(error).__name__}: {error}")
        return False


def imports():
    for module, distribution in [
        ("gymnasium", "gymnasium"), ("mujoco", "mujoco"),
        ("stable_baselines3", "stable-baselines3"), ("torch", "torch"),
        ("tensorboard", "tensorboard"), ("numpy", "numpy"),
        ("imageio_ffmpeg", "imageio-ffmpeg"),
    ]:
        importlib.import_module(module)
        print(f"  {distribution} {version(distribution)}")
    importlib.import_module("gymnasium.envs.mujoco")
    importlib.import_module("tensorboard.default")


def cpu():
    import torch
    assert (torch.tensor([1.0, 2.0], device="cpu") ** 2).sum().item() == 5.0


def encoder():
    import imageio_ffmpeg
    print(f"  FFmpeg {imageio_ffmpeg.get_ffmpeg_version()}")


def physics():
    import mujoco
    import numpy as np
    model = mujoco.MjModel.from_xml_string(FIXTURE)
    data = mujoco.MjData(model)
    for _ in range(10):
        mujoco.mj_step(model, data)
    assert data.time > 0 and np.isfinite(data.qpos).all() and data.qpos[0] < 0


def render(viewer):
    import mujoco
    model = mujoco.MjModel.from_xml_string(FIXTURE)
    if viewer:
        from onboarding.viewer import view_model
        view_model(model, seconds=3)
    else:
        data = mujoco.MjData(model)
        mujoco.mj_forward(model, data)
        with mujoco.Renderer(model, height=480, width=640) as renderer:
            renderer.update_scene(data)
            frame = renderer.render()
            assert frame.shape == (480, 640, 3) and frame.std() > 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--viewer", action="store_true", help="open a 3-second interactive viewer")
    parser.add_argument("--rgb", action="store_true", help="check offscreen rendering separately")
    args = parser.parse_args()
    print(platform.platform(), platform.machine(), platform.python_version())
    checks = [check("packages", imports), check("CPU tensor", cpu),
              check("video encoder", encoder), check("physics", physics)]
    if args.viewer:
        checks.append(check("viewer", lambda: render(True)))
    if args.rgb:
        checks.append(check("RGB renderer", lambda: render(False)))
    raise SystemExit(0 if all(checks) else 1)


if __name__ == "__main__":
    main()
