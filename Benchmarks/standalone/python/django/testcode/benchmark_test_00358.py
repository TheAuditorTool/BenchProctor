# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import db
import os
import pika


def _amqp_receive(queue):
    with pika.BlockingConnection(pika.URLParameters(os.environ.get("AMQP_URL", "amqp://guest:guest@broker:5672/%2F"))) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return channel.basic_get(queue=queue, auto_ack=True)[2]

def BenchmarkTest00358(request):
    msg_value = (_amqp_receive('app-events') or b'').decode()
    if not re.fullmatch("^(asc|desc|name|created)$", str(msg_value)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = msg_value
    db.execute('SELECT * FROM users ORDER BY ' + str(processed))
    return JsonResponse({"saved": True})
