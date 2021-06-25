#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for mbf_align.

    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import pytest
import sys
import subprocess
import pathlib

import pypipegraph2  # noqa:F401

pypipegraph2.replace_ppg1()  # noqa:F401


from pypipegraph.testing.fixtures import (  # noqa:F401
    new_pipegraph,
    pytest_runtest_makereport,
)

from mbf_externals.testing.fixtures import create_local_store  # noqa:F401
from mbf_qualitycontrol.testing.fixtures import new_pipegraph_no_qc  # noqa:F401

root = pathlib.Path(__file__).parent.parent


@pytest.fixture
def local_store():
    local_store_path = root / "tests" / "run" / "local_store"
    local_store_path.mkdir(exist_ok=True, parents=True)
    yield from create_local_store(local_store_path)


print("root", root)
sys.path.append(str(root / "src"))
print("the path is", sys.path)
subprocess.check_call(["python3", "setup.py", "build_ext", "-i"], cwd=root)
