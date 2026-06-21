# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest22608(request):
    xml_value = request.body.decode('utf-8')
    data = normalise_input(xml_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
