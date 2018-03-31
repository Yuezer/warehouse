import allure


class Test_allure:
    def setup(self):
        pass
    def teardown(self):
        pass
    @allure.step("我是测试步骤001")       #添加测试步骤
    def test_al1(self):
        allure.attach('描述','我是测试第一步的描述')    #添加测试描述
        assert 1

    @allure.step("我是测试步骤002")       #添加测试步骤
    def test_al2(self):
        assert 1

    @allure.step("我是测试步骤003")       #添加测试步骤
    def test_al3(self):
        assert 0