import pytest
from reminder import Task

@pytest.fixture(scope="module")
def task_list():
    return [Task(name="pay rent"), Task(name="buy bread")]