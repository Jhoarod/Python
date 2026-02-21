class LoginPage(BasePage):

    USER = (By.ID, "userid")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginBtn")

    def login(self, user, password):
        self.write(self.USER, user)
        self.write(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
