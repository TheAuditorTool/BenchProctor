# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest13160(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    trusted_claim = str(json_value)
    return JsonResponse({'trusted': trusted_claim}, status=200)
