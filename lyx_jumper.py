import webbrowser
import urllib.parse
import win32clipboard

def get_clipboard_data():
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	return data

def get_formatted_data(data):
	return urllib.parse.quote(data)

formatted_data = get_formatted_data(get_clipboard_data())
url = f'https://www.wolframalpha.com/input?i={formatted_data}'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(url)