#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `testproject` package."""

import pytest  # noqa
import testproject


def test_assert():

    assert testproject.__version__ is not None
