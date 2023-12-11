import logging

from flask import Flask, request

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/api/v1', methods=['GET'])
def index():
    args = request.args
    if len(args) <= 0:
        logger.error("Prompt query is not nullable")
    else:
        prompt = args.get("prompt")

    return f"<h1>{prompt}</h1>"


def main(port=8000):
    print(f"Api server is running {port} port")
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
