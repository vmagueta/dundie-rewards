import pytest

from dundie.core import load

from .constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_2_people(request):
    """Test load function has 2 people."""
    assert len(load(PEOPLE_FILE)) == 3


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_j(request):
    """Test load function starts with letter J."""
    assert load(PEOPLE_FILE)[0][0] == "J"
