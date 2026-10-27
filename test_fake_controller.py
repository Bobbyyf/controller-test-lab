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

def test_drains_lowers_battery(new_fake_controller):
    new_fake_controller.drain(30)
    assert new_fake_controller.battery == 70

def test_drain_never_goes_below_zero(new_fake_controller):
    new_fake_controller.drain(150)
    assert new_fake_controller.battery == 0

