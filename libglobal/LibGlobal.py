from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import openpyxl


class Base:
    def launch_browser(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\k_sur\8056\Selenium5.00PM\driver\chromedriver.exe")
        self.driver.implicitly_wait(10)
        return self.driver

    # WebDriver
    def window_maximize(self):
        self.driver.maximize_window()

    def window_minimize(self):
        self.driver.minimize_window()

    def load_url(self, url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def close_window(self):
        self.driver.close()

    def capture_page(self, file_name):
        self.driver.save_screenshot(file_name)

    def refresh_page(self):
        self.driver.refresh()

    def go_to(self):
        self.driver.forward()

    def go_back(self):
        self.driver.back()

    def page_url(self):
        url = self.driver.current_url
        return url

    def get_current_window_id(self):
        par_id = self.driver.current_window_handle
        return par_id

    def get_all_windows_id(self):
        all_windows_id = self.driver.window_handles
        return all_windows_id

    def page_title(self):
        t = self.driver.title
        return t

    # WebElement
    def fill(self, e, data):
        e.send_keys(data)

    def btn_click(self, ele):
        ele.click()

    def attribute_value(self, e, name):
        e.get_attribute(name)

    def enabled(self, x):
        enabled = x.is_enabled()
        return enabled

    def displayed(self, y):
        dis = y.is_displayed()
        return dis

    def selected(self, z):
        s = z.is_selected()
        return s

    def get_text(self, el):
        t = el.text
        return t

    # Alert
    def switch_alert(self):
        al = self.driver.switch_to.alert
        return al

    def alert_ok(self):
        al = self.switch_alert()
        al.accept()

    def alert_cancel(self):
        al = self.switch_alert()
        al.dismiss()

    def fill_alert(self, data):
        al = self.switch_alert()
        al.send_keys(data)

    def get_text_from_alert(self):
        al = self.switch_alert()
        t = al.text
        return t

    # ActionChains
    def mouse_over(self, e):
        a = ActionChains(self.driver)
        a.move_to_element(e).perform()

    def drag_drop(self, src, des):
        a = ActionChains(self.driver)
        a.drag_and_drop(src, des).perform()

    def right_click(self, e):
        a = ActionChains(self.driver)
        a.context_click(e).perform()

    def double_tab(self, e):
        a = ActionChains(self.driver)
        a.double_click(e).perform()

    def switch_frame_by_id(self, id):
        self.driver.switch_to.frame(id)

    def switch_frame_by_name(self, name):
        self.driver.switch_to.frame(name)

    def switch_frame_by_index(self, i):
        self.driver.switch_to.frame(i)

    def switch_frame_by_element(self, e):
        self.driver.switch_to.frame(e)

    # Select
    def dd_by_index(self, ele, i):
        s = Select(ele)
        s.select_by_index(i)

    def dd_by_value(self, ele, value):
        s = Select(ele)
        s.select_by_value(value)

    def dd_by_text(self, ele, text):
        s = Select(ele)
        s.select_by_visible_text(text)

    def deselect_index(self, e, i):
        s = Select(e)
        s.deselect_by_index(i)

    def deselect_value(self, e, value):
        s = Select(e)
        s.deselect_by_value(value)

    def deselect_text(self, e, text):
        s = Select(e)
        s.deselect_by_visible_text(text)

    def all_deselect(self, e):
        s = Select(e)
        s.deselect_all()

    def dd_options(self, e):
        s = Select(e)
        op = s.options
        return op

    def get_data_from_excel(self, excel_loc, row, cell):
        w = openpyxl.load_workbook(excel_loc)
        sheet = w.active
        c = sheet.cell(row, cell)
        data = c.value
        return data
