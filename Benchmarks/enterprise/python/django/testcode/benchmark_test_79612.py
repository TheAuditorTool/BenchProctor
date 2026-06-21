# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest79612(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    requests.get(str(data))
    return JsonResponse({"saved": True})
