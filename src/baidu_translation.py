from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def translate(driver: WebDriver, text):
    driver.get("https://fanyi.baidu.com/")
    driver.implicitly_wait(1)
    # 关闭模态框
    driver.find_element(By.XPATH, "//*[@id=\"desktop-guide-wrapper\"]/div/div/div/a[2]").click()
    driver.implicitly_wait(0.5)

    # 输入要翻译的内容
    driver.find_element(By.ID, "baidu_translate_input").send_keys(text)
    driver.find_element(By.ID, "translate-button").click()
    driver.implicitly_wait(1.5)
    result = driver.find_element(By.XPATH,
                                 "//*[@id=\"main-outer\"]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/p[2]").text

    return result


def main(text):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')  # 无头浏览器
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    result = translate(driver, text)
    print("原文：", text)
    print("译文：", result)
    driver.quit()


if __name__ == '__main__':
    inp_text = input("请输入要翻译的内容：").strip()
    main(inp_text)
