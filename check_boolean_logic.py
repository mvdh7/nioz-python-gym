import numpy as np
from setup_boolean_logic import temperature, salinity, _testarr


def ex0(func0):
    """Return the sum of two numbers (x and y)."""
    assert func0(2, 2) == 4, "func0: something's not quite right..."
    assert np.all(
        np.isclose(func0(_testarr, 3), _testarr + 3)
    ), "func0: something's not quite right..."
    print("Exercise 0 passed!")


def _check_temperature_shape(answer, funcX):
    """Check if the answer has the same shape and size as temperature."""
    assert not isinstance(
        answer, bool
    ), "{}: your output should be an array of True values, not just a single one!".format(
        funcX,
    )
    assert len(temperature) == len(
        answer
    ), "{}: your output contains {} element(s), but temperature contains {}!".format(
        funcX, len(answer), len(temperature)
    )
    assert np.shape(temperature) == np.shape(
        answer
    ), "{}: your output has the shape {}, but temperature has the shape {}!".format(
        funcX, np.shape(answer), np.shape(temperature)
    )


def ex1(func1):
    """Return True where input array (i.e. temperature) is greater than 18."""
    _check_temperature_shape(func1(temperature), "func1")
    assert np.all(
        func1(temperature) == (temperature > 18)
    ), "func1: something's not quite right..."
    assert np.all(
        func1(_testarr) == (_testarr > 18)
    ), "func1: something's not quite right..."
    print("Exercise 1 passed!")


# def ex2(answer):
#     """Create an array of False values, the same shape as temperature."""
#     _check_temperature_shape(answer)
#     assert not np.any(answer), "not all of the elements of your answer are False!"
#     print("Exercise 2 passed!")


# def ex3(answer):
#     """Create an array that is True where temperature is greater than 18."""
#     _check_temperature_shape(answer)
#     assert np.all(
#         temperature[answer] > 18
#     ), "not all your True values correspond to temperatures greater than 18!"
#     assert not np.any(
#         temperature[~answer] > 18
#     ), "not all temperatures greater than 18 are True in your answer!"
#     print("Exercise 3 passed!")


# def ex4(answer):
#     """Create an array that is True where temperature is greater than 18, and less than
#     or equal to 21.
#     """
#     _check_temperature_shape(answer)
#     assert np.all(
#         temperature[answer] > 18
#     ), "not all your True values correspond to temperatures greater than 18!"
#     assert np.all(
#         temperature[answer] <= 21
#     ), "not all your True values correspond to temperatures less than or equal to 21!"
#     tna = temperature[~answer]
#     assert not np.any((tna > 18) & (tna <= 21)), (
#         "your answer does not capture all temperatures greater than 18 and "
#         + "less than or equal to 21!"
#     )
#     print("Exercise 4 passed!")


# def ex5(answer):
#     """Create an array that is True where temperature is less than or equal to 18, or
#     more than 21.
#     """
#     _check_temperature_shape(answer)
#     assert np.all((temperature[answer] <= 18) | (temperature[answer] > 21)), (
#         "not all your True values correspond to temperatures less than or equal to 18,"
#         + " or more than 21!"
#     )
#     tna = temperature[~answer]
#     assert not np.any((tna <= 18) | (tna > 21)), (
#         "your answer does not capture all temperatures less than or equal to 18, or "
#         + "greater than 21!"
#     )
#     print("Exercise 5 passed!")


# def ex6(answer):
#     """Create an array that is True where temperature is in the ranges specified in
#     Ex. 5, and salinity is less than or equal to 35.
#     """
#     _check_temperature_shape(answer)
#     assert np.all((temperature[answer] <= 18) | (temperature[answer] > 21)), (
#         "not all your True values correspond to temperatures less than or equal to 18,"
#         + " or more than 21!"
#     )
#     assert np.all(
#         salinity[answer] <= 35
#     ), "not all your True values correspond to salinities less than or equal to 35!"
#     tna = temperature[~answer]
#     assert not np.any(
#         ((tna <= 18) | (tna > 21)) & (salinity[~answer] <= 35)
#     ), "your answer does not capture all the requested values!"
#     print("Exercise 6 passed!")


# def ex7(answer):
#     """Create an array that is True where temperature is exactly 21 or salinity is
#     exactly 35.
#     """
#     _check_temperature_shape(answer)
#     assert np.all((temperature[answer] == 21) | (salinity[answer] == 35)), (
#         "some of your True values correspond to neither the specified temperature "
#         + "nor salinity!"
#         ""
#     )
#     assert not np.any(
#         (temperature[~answer] == 21) | (salinity[~answer] == 35)
#     ), "your answer does not capture all the requested values!"
#     print("Exercise 7 passed!")


# def ex8(func):
#     """Is every element in the answer to Ex. 1 True?"""
#     answer = func(np.full_like(temperature, True))
#     assert isinstance(answer, bool), "your answer must be a single True or False value!"
#     assert answer, """your answer should be True!"""
#     print("Exercise 8 passed!")


# def ex9(answer):
#     """Is every element in your answer to Ex. 9 False?"""
#     assert isinstance(answer, bool), "your answer must be a single True or False value!"
#     assert answer, "your answer should be True!"
#     print("Exercise 9 passed!")


# def ex10(answer):
#     """Are there are any points where temperature is less than 4 and salinity is
#     greater than 40?
#     """
#     assert isinstance(answer, bool), "your answer must be a single True or False value!"
#     assert answer, "your answer should be True!"
#     print("Exercise 10 passed!")
