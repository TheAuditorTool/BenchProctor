# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest49277(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
