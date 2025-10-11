from software_design_HW1.src.container import Container


def test_container():
    c = Container()

    a1 = c.resolve("animal_service")
    a2 = c.resolve("animal_service")
    t1 = c.resolve("thing_service")
    t2 = c.resolve("thing_service")

    assert a1 == a2
    assert t1 == t1

    assert a1.number_registry is t1.number_registry
