import bardconnection
import config

question = "How can ı install maven?"


def main():
    cnf = config.Config()
    bardconnection.get_connection(question, cnf.get_bard_api_key())


if __name__ == '__main__':
    main()
