# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest00062(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    digest = hashlib.sha3_256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
