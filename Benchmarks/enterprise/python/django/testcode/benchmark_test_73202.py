# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest73202(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
