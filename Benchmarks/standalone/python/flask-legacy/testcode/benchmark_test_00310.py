# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
from flask import Flask, jsonify
import os
import pika
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


def _amqp_receive(queue):
    with pika.BlockingConnection(pika.URLParameters(os.environ.get("AMQP_URL", "amqp://guest:guest@broker:5672/%2F"))) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return channel.basic_get(queue=queue, auto_ack=True)[2]
_engine = create_engine("sqlite:///" + os.environ.get("DATABASE_PATH", "app.db"))
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00310", methods=["POST"])
def BenchmarkTest00310():
    msg_value = (_amqp_receive('app-events') or b'').decode()
    if msg_value:
        data = msg_value
    else:
        data = ''
    with Session(_engine) as _session:
        _session.query(User).from_statement(text('SELECT * FROM "' + str(data).replace('"', '""') + '"')).all()
    return jsonify({"result": "success"})
