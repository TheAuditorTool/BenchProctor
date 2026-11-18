# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
import re
from app_runtime import db
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


@app.route("/BenchmarkTest00253", methods=["POST"])
def BenchmarkTest00253():
    msg_value = (_amqp_receive('app-events') or b'').decode()
    if not re.fullmatch("^(asc|desc|name|created)$", str(msg_value)):
        return jsonify({'error': 'forbidden'}), 400
    processed = msg_value
    db.execute('SELECT * FROM users ORDER BY ' + str(processed))
    return jsonify({"result": "success"})
