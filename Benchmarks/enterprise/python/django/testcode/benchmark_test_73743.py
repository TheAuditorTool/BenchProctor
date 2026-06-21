# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest73743(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
