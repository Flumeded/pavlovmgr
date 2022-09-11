import constant
import server_handler
import  exceptions


def __main__():
    try:
        server = server_handler.Server(constant.SERVER_ID)
        server.start()
    except exceptions.ServerStatusError as err:
        print(f"Error with server status: {str(err)}")


__main__()
