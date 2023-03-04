import json
from importlib.resources import files

from dly_algs import deep_merge, deep_compare
import pytest

TEST_RESOURCES = "tests.resources"
DEEP_COMPARE_TEST_DATA = json.loads(files(TEST_RESOURCES).joinpath("deep_compare_test_data.json").read_text())
DEEP_MERGE_TEST_DATA = json.loads(files(TEST_RESOURCES).joinpath("deep_merge_test_data.json").read_text())


@pytest.mark.parametrize("test_data", DEEP_MERGE_TEST_DATA)
def test_deep_merge(test_data) -> None:
    x_dict: dict = test_data.get("x_dict")
    y_dict: dict = test_data.get("y_dict")
    expected: dict = test_data.get("expected")

    merged = deep_merge(x_dict, y_dict)
    assert deep_compare(merged, expected)


@pytest.mark.parametrize("test_data", DEEP_COMPARE_TEST_DATA)
def test_deep_compare(test_data: dict) -> None:
    x_dict: dict = test_data.get("x_dict")
    y_dict: dict = test_data.get("y_dict")
    expected: bool = test_data.get("expected")

    assert deep_compare(x_dict, y_dict) is expected
