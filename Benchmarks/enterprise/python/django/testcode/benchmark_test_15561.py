# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest15561(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
