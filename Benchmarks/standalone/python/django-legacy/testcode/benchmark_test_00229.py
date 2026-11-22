# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
import pika
import importlib


def _amqp_receive(queue):
    with pika.BlockingConnection(pika.URLParameters(os.environ.get("AMQP_URL", "amqp://guest:guest@broker:5672/%2F"))) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return channel.basic_get(queue=queue, auto_ack=True)[2]
def _revive_typed(fields):
    type_name = fields.pop('__type__', None)
    if type_name is None:
        return fields
    module_name, _, class_name = type_name.rpartition('.')
    return getattr(importlib.import_module(module_name), class_name)(**fields)

def BenchmarkTest00229(request):
    msg_value = (_amqp_receive('app-events') or b'').decode()
    data = '%s' % (msg_value,)
    parsed = json.JSONDecoder(object_hook=_revive_typed).decode(str(data))
    return JsonResponse({'parsed': str(parsed)}, status=200)
