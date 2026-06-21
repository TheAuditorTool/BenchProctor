# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest73273(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
