from fake_controller import FakeController

def test_new_controller_has_nothing_pressed():
    controller = FakeController()
    result = controller.is_pressed("cross")
    assert result is False

def test_press_then_release():
    controller = FakeController()
    controller.press("cross")
    result = controller.is_pressed("cross")
    assert result is True
    controller.release("cross")
    result = controller.is_pressed("cross")
    assert result is False

def test_drains_lowers_battery():
    controller = FakeController()
    result = controller.drain(30)
    assert result is controller.battery == 70

def test_drain_never_goes_below_zero():
    controller = FakeController()
    result = controller.drain(150)
    assert result is controller.battery == 0