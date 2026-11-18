# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import os
import pika


def _amqp_receive(queue):
    with pika.BlockingConnection(pika.URLParameters(os.environ.get("AMQP_URL", "amqp://guest:guest@broker:5672/%2F"))) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return channel.basic_get(queue=queue, auto_ack=True)[2]

def BenchmarkTest00449(request):
    msg_value = (_amqp_receive('app-events') or b'').decode()
    data = f'{msg_value!s}'
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
