# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import db
import os
import pika


def _amqp_receive(queue):
    with pika.BlockingConnection(pika.URLParameters(os.environ.get("AMQP_URL", "amqp://guest:guest@broker:5672/%2F"))) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return channel.basic_get(queue=queue, auto_ack=True)[2]

bp = Blueprint("annotate_digest", __name__)


@bp.route("/annotate_digest", methods=["POST"])
def annotate_digest():
    preface = (_amqp_receive('app-events') or b'').decode()
    remark = (lambda v: v.strip())(preface)
    db.execute("SELECT * FROM users WHERE id = '" + str(remark) + "'")
    return jsonify({"result": "success"})
