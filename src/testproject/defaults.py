# -*- coding: utf-8 -*-
import os
import sys

from appdirs import AppDirs


testproject_app_dirs = AppDirs("testproject", "frkl")

if not hasattr(sys, "frozen"):
    TESTPROJECT_MODULE_BASE_FOLDER = os.path.dirname(__file__)
    """Marker to indicate the base folder for the `testproject` module."""
else:
    TESTPROJECT_MODULE_BASE_FOLDER = os.path.join(
        sys._MEIPASS, "testproject"  # type: ignore
    )
    """Marker to indicate the base folder for the `testproject` module."""

TESTPROJECT_RESOURCES_FOLDER = os.path.join(TESTPROJECT_MODULE_BASE_FOLDER, "resources")
