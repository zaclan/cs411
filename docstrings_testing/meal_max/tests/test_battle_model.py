import logging
from typing import List

import pytest

from meal_max.models.kitchen_model import Meal, update_meal_stats
from meal_max.models.battle_model import BattleModel
from meal_max.utils.logger import configure_logger

# Configure the logger for testing
logger = logging.getLogger(__name__)
configure_logger(logger)

######################################################
#
#    Fixtures
#
######################################################

@pytest.fixture
def battle_model():
    """Fixture to create a new instance of BattleModel for each test."""
    return BattleModel()

@pytest.fixture
def mock_update_meal_stats(mocker):
    """Fixture to mock the update_meal_stats function."""
    return mocker.patch('meal_max.models.battle_model.update_meal_stats')

@pytest.fixture
def mock_get_random(mocker):
    """Fixture to mock the get_random function."""
    return mocker.patch('meal_max.models.battle_model.get_random', return_value=0.5)


"""Fixtures providing sample meals for the tests"""
@pytest.fixture
def sample_meal1():
    return Meal(id=1, meal="Spaghetti", cuisine="Italian", price=12.99, difficulty="MED")

@pytest.fixture
def sample_meal2():
    return Meal(id=2, meal="Sushi", cuisine="Japanese", price=15.50, difficulty="HIGH")

@pytest.fixture
def sample_meal3():
    return Meal(id=3, meal="Burrito", cuisine="Mexican", price=8.99, difficulty="LOW")

@pytest.fixture
def sample_meal4():
    return Meal(id=1, meal="Meal1", cuisine="Cuisine1", price=10.0, difficulty="LOW")

@pytest.fixture
def sample_meal5():
    return Meal(id=2, meal="Meal2", cuisine="Cuisine2", price=5.0, difficulty="HIGH")


######################################################
#
#    Add, Get, Clear
#
######################################################
    
def test_prep_combatant(battle_model, sample_meal1):
    """Test adding a combatant to the battle."""
    battle_model.prep_combatant(sample_meal1)
    assert battle_model.combatants == [sample_meal1]

def test_prep_combatant_full(battle_model, sample_meal1, sample_meal2, sample_meal3):
    """Test that adding a third combatant raises an error."""
    
    battle_model.prep_combatant(sample_meal1)
    battle_model.prep_combatant(sample_meal2)
    
    with pytest.raises(ValueError, match="Combatant list is full, cannot add more combatants."):
        battle_model.prep_combatant(sample_meal3)


def test_get_combatant(battle_model, sample_meal1, sample_meal2):
    """Test retrieving the list of combatants."""
    battle_model.prep_combatant(sample_meal1)
    battle_model.prep_combatant(sample_meal2)
    combatants = battle_model.get_combatants()
    assert combatants == [sample_meal1, sample_meal2], "Expected to retrieve the list of prepared combatants."

def test_clear_combatants(battle_model, sample_meal1):
    """Test clearing the combatants list."""
    battle_model.prep_combatant(sample_meal1)
    combatants = battle_model.get_combatants()
    assert combatants == [sample_meal1], "Expected to have one combatant before clearing"
    battle_model.clear_combatants()
    assert battle_model.combatants == [], "Expected combatants list to be empty after clearing."

def test_clear_empty_combatants(battle_model, caplog):
    """Test clearing an already empty combatants list and check logging."""
    battle_model.clear_combatants()
    assert len(battle_model.get_combatants()) == 0, "Combatants list should be empty after clearing"
    assert "Clearing the combatants list." in caplog.text, "Expected log message when clearing combatants list"
    
######################################################
#
#    Battle
#
######################################################

def test_battle_model_initialization(battle_model):
    """Test that the BattleModel initializes with an empty combatants list."""
    assert battle_model.combatants == []

def test_get_battle_score(battle_model, sample_meal1):
    """Test calculating the battle score for a combatant."""
    score = battle_model.get_battle_score(sample_meal1)
    expected_score = (12.99 * len("Italian")) - 2  # Difficulty modifier for "MED" is 2
    assert score == expected_score, f"Expected battle score {expected_score}, got {score}"

def test_battle_win_combatant_1(battle_model, mock_update_meal_stats, mock_get_random, sample_meal4, sample_meal5):
    """Test a battle where combatant 1 wins."""
    # Mock get_random to return a value that ensures combatant 1 wins
    mock_get_random.return_value = 0.1

    battle_model.prep_combatant(sample_meal4)
    battle_model.prep_combatant(sample_meal5)
    
    winner = battle_model.battle()
    
    assert winner == "Meal1", f"Expected winner to be 'Meal1', got '{winner}'"
    assert battle_model.combatants == [sample_meal4], "Expected combatants list to contain only the winner."

    # Check that update_meal_stats was called correctly
    mock_update_meal_stats.assert_any_call(sample_meal4.id, 'win')
    mock_update_meal_stats.assert_any_call(sample_meal5.id, 'loss')

def test_battle_win_combatant_2(battle_model, mock_update_meal_stats, mock_get_random, sample_meal4, sample_meal5):
    """Test a battle where combatant 2 wins."""
    # Mock get_random to return a value that ensures combatant 2 wins
    mock_get_random.return_value = 0.9

    battle_model.prep_combatant(sample_meal4)
    battle_model.prep_combatant(sample_meal5)
    
    winner = battle_model.battle()
    
    assert winner == "Meal2", f"Expected winner to be 'Meal2', got '{winner}'"
    assert battle_model.combatants == [sample_meal5], f"Expected combatants list to contain only the winner, got '{battle_model.combatants}'"

    # Check that update_meal_stats was called correctly
    mock_update_meal_stats.assert_any_call(sample_meal4.id, 'loss')
    mock_update_meal_stats.assert_any_call(sample_meal5.id, 'win')

def test_battle_not_enough_combatants(battle_model, sample_meal1):
    """Test that a battle cannot occur with less than two combatants."""
    battle_model.prep_combatant(sample_meal1)

    with pytest.raises(ValueError, match="Two combatants must be prepped for a battle."):
        battle_model.battle()

def test_battle_no_combatants(battle_model):
    """Test that a battle cannot occur with no combatants."""
    with pytest.raises(ValueError, match="Two combatants must be prepped for a battle."):
        battle_model.battle()