import config
import webapi

question = "How can ı install maven?"


def main():
    cnf = config.Config()
    webapi.main(cnf.get_api_test_port())
    # async
    # bardconnection.get_connection(question, cnf.get_bard_api_key())


if __name__ == '__main__':
    main()
