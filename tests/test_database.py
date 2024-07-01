"""Tests the database."""

import pytest

from dundie.database import EMPTY_DB, add_movement, add_person, commit, connect


@pytest.mark.unit
def test_database_schema():
    """Test the schema of database."""
    db = connect()
    assert db.keys() == EMPTY_DB.keys()


@pytest.mark.unit
def test_commit_to_database():
    """Test the function commit to the database."""
    db = connect()
    data = {"name": "Joe Doe", "role": "Salesman", "dept": "Sales"}
    db["people"]["joe@doe.com"] = data
    commit(db)

    db = connect()
    assert db["people"]["joe@doe.com"] == data


@pytest.mark.unit
def test_add_person_for_the_first_time():
    """Test the add person to the db for the first time."""
    pk = "joe@doe.com"
    data = {"role": "Salesman", "dept": "Sales", "name": "Joe Doe"}
    db = connect()
    person, created = add_person(db, pk, data)
    assert created is True
    commit(db)

    db = connect()
    assert db["people"][pk] == data
    assert db["balance"][pk] == 500
    assert len(db["movement"][pk]) > 0
    assert db["movement"][pk][0]["value"] == 500


@pytest.mark.unit
def test_negative_add_person_invalid_email():
    """Test if invalid email is going to raise a Value Error."""
    with pytest.raises(ValueError):
        add_person({}, ".@bla", {})


@pytest.mark.unit
def test_add_or_remove_points_for_person():
    """Test add two persons and add and remove points of them."""
    pk = "joe@doe.com"
    data = {"role": "Salesman", "dept": "Sales", "name": "Joe Doe"}
    db = connect()
    person, created = add_person(db, pk, data)
    assert created is True
    commit(db)

    db = connect()
    before = db["balance"][pk]

    add_movement(db, pk, -100, "manager")
    commit(db)

    db = connect()
    after = db["balance"][pk]

    assert after == before - 100
    assert after == 400
    assert before == 500
