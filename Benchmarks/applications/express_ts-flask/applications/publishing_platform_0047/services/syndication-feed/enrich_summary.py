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

bp = Blueprint("enrich_summary", __name__)


@bp.route("/enrich_summary", methods=["POST"])
def enrich_summary():
    synopsis = (_amqp_receive('app-events') or b'').decode()
    byline = (lambda v: v.strip())(synopsis)
    pickle.loads(base64.b64decode(byline))
    return jsonify({"result": "success"})
