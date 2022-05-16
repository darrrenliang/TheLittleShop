# import pytest

# def func(x):
#     return x + 5

# def test_method():
#     assert func(3) == 5

# @pytest.fixture
# def example_people_data():
#     return [
#         {
#             "given_name": "Alfonsa",
#             "family_name": "Ruiz",
#             "title": "Senior Software Engineer",
#         }
#     ]

# @pytest.mark.parametrize("non_palindrome", [
#     "abc",
#     "abab",
# ])
# def test_is_palindrome_not_palindrome(non_palindrome):
#     assert not is_palindrome(non_palindrome)

# @pytest.mark.parametrize("maybe_palindrome, expected_result", [
#     ("", True),
#     ("a", True),
#     ("Bob", True),
#     ("Never odd or even", True),
#     ("Do geese see God?", True),
#     ("abc", False),
#     ("abab", False),
# ])
# def test_is_palindrome(maybe_palindrome, expected_result):
#     assert is_palindrome(maybe_palindrome) == expected_result