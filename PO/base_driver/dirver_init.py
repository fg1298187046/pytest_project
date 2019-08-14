from appium import webdriver


def base_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = '1111'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = 'com.oppo.settings.SettingsActivity'
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    return driver
