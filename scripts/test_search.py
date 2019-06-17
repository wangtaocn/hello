import allure

from base.base_driver import init_driver
from page.page import Page

import pytest

class TestSearch:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
    # @allure.step(title = "设置项目")
    @pytest.mark.parametrize("keyword", ["xiaoming", "123", "hello"])
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_search(self, keyword):
        self.page.setting.click_search()
        self.page.search.input_search(keyword)
        self.page.search.click_back()
