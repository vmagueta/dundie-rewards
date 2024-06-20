import pytest
from subprocess import check_output


@pytest.mark.integration
@pytest.mark.medium
def test_load():
    """Test command load"""
    out = check_output(
        ["dundie", "load", "assets/people.csv"]
    ).decode("utf-8").split("\n")
    assert len(out) == 2
