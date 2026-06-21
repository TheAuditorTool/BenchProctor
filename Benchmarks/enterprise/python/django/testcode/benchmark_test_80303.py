# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest80303(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
