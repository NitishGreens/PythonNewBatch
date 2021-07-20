from libglobal.LibGlobal import Base
from PageObject.pages.LoginPage import LoginPage


class Employee(Base):
    # self ---> it hold current object reference
    def login(self):
        driver = self.launch_browser()
        self.window_maximize()
        self.load_url("https://en-gb.facebook.com/")
        l = LoginPage(driver)
        self.fill(l.getTxtUserName(),
                  self.get_data_from_excel(r"C:\Users\k_sur\8056\Selenium7.00PM\Excel\Sample.xlsx", 2, 1))
        self.fill(l.getTxtPassword(),
                  self.get_data_from_excel(r"C:\Users\k_sur\8056\Selenium7.00PM\Excel\Sample.xlsx", 2, 2))
        self.btn_click(l.getBtnLogin())
        self.quit_browser()


e = Employee()
e.login()
