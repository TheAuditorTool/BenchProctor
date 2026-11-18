# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
import base64
import pickle
import os
import pika


def _amqp_receive(queue):
    with pika.BlockingConnection(pika.URLParameters(os.environ.get("AMQP_URL", "amqp://guest:guest@broker:5672/%2F"))) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return channel.basic_get(queue=queue, auto_ack=True)[2]

bp = Blueprint("summarize_trace", __name__)


@bp.route("/summarize_trace", methods=["POST"])
def summarize_trace():
    caption = (_amqp_receive('app-events') or b'').decode()
    gauge = (lambda v: v.strip())(caption)
    pickle.loads(base64.b64decode(gauge))
    return jsonify({"result": "success"})
