# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest16849(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    auth_check('user', data)
    return JsonResponse({"saved": True})
