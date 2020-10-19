# This is a sample South African Lottery Python script.
# To execute it on PyCharm:         Press -> Shift+F10
# To execute it on the Terminal:    Type  -> python main.py

from resource.server import start_server


def start_flask_api_server(host="0.0.0.0", port=5000, debug=True):
    # Use a breakpoint in the code line below to debug your script.
    return start_server(host, port, debug)  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script; on PyCharm
if __name__ == '__main__':
    start_flask_api_server()  # this will runs start_flask_api_server with default parameter arguments.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
