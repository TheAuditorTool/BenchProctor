# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest20372(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
