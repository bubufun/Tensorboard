from multiprocessing import Process
from tensorboard.program import TensorBoard
from flask import Flask, jsonify

app = Flask(__name__)


def tensorboard_main(host, port, logdir):
    configuration = list([""])
    configuration.extend(["--host", host])
    configuration.extend(["--port", port])
    configuration.extend(["--logdir", logdir])

    tensorboard = TensorBoard()
    tensorboard.configure(configuration)
    tensorboard.main()


# def flask_main(app, host, port):
#     return app.run(host=host, port=port)
#
#
# @app.route("/hello-world", methods=["GET", "POST"])
# def say_hello():
#     return jsonify({"result": "Hello world"})



if __name__ == "__main__":
    host = "0.0.0.0"
    port_for_tensorboard = "6006"
    # port_for_flask = "5000"
    logdir = "./BASKET_SUM_COMM_embedding_log"
    process_for_tensorboard = Process(target=tensorboard_main, args=(host, port_for_tensorboard, logdir))
    # process_for_flask = Process(target=flask_main, args=(app, host, port_for_flask))
    process_for_tensorboard.start()
    # process_for_flask.start()
    process_for_tensorboard.join()
    # process_for_flask.join()