from fake_controller import FakeController
import pytest

@pytest.fixture
def new_fake_controller():
    controller = FakeController()
    return controller

def test_new_controller_has_nothing_pressed(new_fake_controller):
    result = new_fake_controller.is_pressed("cross")
    assert result is False

def test_press_then_release(new_fake_controller):
    new_fake_controller.press("cross")
    result = new_fake_controller.is_pressed("cross")
    assert result is True
    new_fake_controller.release("cross")
    result = new_fake_controller.is_pressed("cross")
    assert result is False

@pytest.mark.parametrize("amount, expected", [(30,70), (15,85), (92, 8), (150, 0), (100, 0), (0, 100)])

def test_drain(new_fake_controller, amount, expected):
    new_fake_controller.drain(amount)
    assert new_fake_controller.battery == expected

def test_drain_negative_val(new_fake_controller):
    with pytest.raises(ValueError, match = "Battery cannot be over 100"):
        new_fake_controller.drain(-10)