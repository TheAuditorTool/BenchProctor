# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Flask, jsonify
import os
import pika


def _amqp_receive(queue):
    with pika.BlockingConnection(pika.URLParameters(os.environ.get("AMQP_URL", "amqp://guest:guest@broker:5672/%2F"))) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return channel.basic_get(queue=queue, auto_ack=True)[2]

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00049", methods=["POST"])
def BenchmarkTest00049():
    msg_value = (_amqp_receive('app-events') or b'').decode()
    data = f'{msg_value!s}'
    parsed = yaml.safe_load(data)
    return jsonify({'parsed': str(parsed)}), 200
