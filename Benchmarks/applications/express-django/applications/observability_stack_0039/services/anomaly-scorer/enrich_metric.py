# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import os
import pika


def _amqp_receive(queue):
    with pika.BlockingConnection(pika.URLParameters(os.environ.get("AMQP_URL", "amqp://guest:guest@broker:5672/%2F"))) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return channel.basic_get(queue=queue, auto_ack=True)[2]

@csrf_exempt
def enrich_metric(request):
    caption = (_amqp_receive('app-events') or b'').decode()
    cohort = json.loads(caption).get('value', '')
    parsed = json.loads(cohort)
    return JsonResponse({'parsed': str(parsed)}, status=200)
