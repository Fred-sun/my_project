import allure
# def test_one():
#     assert 1 + 1 == 2

# def test_two():
#     assert 1 + 12 == 2

@allure.epic("Fredy Epic")
@allure.feature("Fredy Feature")
class  TestClass:
    @allure.story("Fredy Story --- test three")
    @allure.title("Fredy Title --- test three")
    @allure.testcase("Fredy Testcase --- test three")
    @allure.issue("Fredy Issue --- test three", name="Issue Link")
    @allure.description("Fredy Description --- test three")
    @allure.step("Fredy Step --- test three")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Fredy Tag1", "Fredy Tag2")
    @allure.link("https://www.baidu.com", name="Baidu Link")
    def test_three(self):
        assert "hello".upper() == "HELLO"

    # def test_four(self):
    #     assert len([1, 2, 3]) == 3
    @allure.story("Fredy Story --- test five")
    @allure.title("Fredy Title --- test five")
    @allure.testcase("Fredy Testcase --- test five")
    @allure.issue("Fredy Issue --- test five", name="Issue Link")
    @allure.description("Fredy Description --- test five")
    @allure.step("Fredy Step --- test five")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("Fredy Tag12", "Fredy Tag22")
    @allure.link("https://www.baidu.com", name="Baidu Link")
    def test_five(self):
        assert sum([1, 2, 3]) == 6




