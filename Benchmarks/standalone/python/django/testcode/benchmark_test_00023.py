# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import base64
import os
import pika


def _amqp_receive(queue):
    with pika.BlockingConnection(pika.URLParameters(os.environ.get("AMQP_URL", "amqp://guest:guest@broker:5672/%2F"))) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return channel.basic_get(queue=queue, auto_ack=True)[2]

def BenchmarkTest00023(request):
    msg_value = (_amqp_receive('app-events') or b'').decode()
    data = base64.b64decode(msg_value).decode('utf-8', 'ignore')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
