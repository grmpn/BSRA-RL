import pytest

from onboarding.env import make_env
from onboarding.train import train


@pytest.fixture
def env():
    environment = make_env()
    yield environment
    environment.close()


@pytest.fixture(scope="session")
def trained_run(tmp_path_factory):
    root = tmp_path_factory.mktemp("training")
    policy = train("smoke", smoke=True, output_dir=root)
    return root, policy
