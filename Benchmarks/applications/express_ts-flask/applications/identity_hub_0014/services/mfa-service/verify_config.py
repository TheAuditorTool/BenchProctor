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

bp = Blueprint("verify_config", __name__)


@bp.route("/verify_config", methods=["POST"])
def verify_config():
    snippet = (_amqp_receive('app-events') or b'').decode()
    persona = (lambda v: v.strip())(snippet)
    pickle.loads(base64.b64decode(persona))
    return jsonify({"result": "success"})
