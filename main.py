import webview
from api import API

api = API()

webview.create_window(
    "Murder Horror",
    "web/index.html",
    js_api=api,
    width=1000,
    height=700
)

webview.start(debug=True)