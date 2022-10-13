import pytest

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'



def test_should_link(browser):
    browser.get(link)
    
if __name__ == '__main__':
    pytest.main()










