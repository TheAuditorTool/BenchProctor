# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle
from app_runtime import mq_client


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest76885(request):
    msg_value = mq_client.get_message().body
    reader = make_reader(msg_value)
    data = reader()
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
