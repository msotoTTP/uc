import undetected_chromedriver as uc
# from pyvirtualdisplay import Display

#on mac, install Xquartz to make this work (that install Xvfb behind the scenes)
# display = Display(visible=False)
# display.start()

def googleTest():
    driver = uc.Chrome()
    driver.get("https://google.com")
    searchBox = driver.execute_script('return document.querySelector("input[type=text][title=Search]")')
    driver.quit()
    assert searchBox is not None

# driver = uc.Chrome()
# url = "https://www.royalcaribbean.com/cruises?search=ship:WN|startDate:2023-02-11~2023-02-14"
# driver.get(url)
# cruise_results = driver.execute_script('return document.getElementById("cruise-results-wrapper")')
# driver.quit()
# assert cruise_results is not None
# print("yo")

def testy(driver, url):
    driver.get(url)
    id = hash(url)
    with open(f"pages/{id}.html", "w") as f:
        f.write(driver.page_source)

if __name__ == "__main__":
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('--disable-dev-shm-usage')        
    driver = uc.Chrome(options=chrome_options)
    while True:
        url = input("Enter a url: ")
        if url == "quit":
            break
        testy(driver, url)
    driver.quit()

#docker build . -t undetected
#docker run -it -v $PWD/pages:/pages --name un-con undetected 
#then run python main.py (maybe add a wait time for the "connection secure" page to pass)