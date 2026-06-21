# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest07158(request):
    secret_value = 'default_config_label'
    data = f'{secret_value:.200s}'
    store_cred = os.environ.get('APP_SECRET', '')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return JsonResponse({"saved": True})
