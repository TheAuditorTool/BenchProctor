# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00066(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % str(ua_value)
    digest = hashlib.sha3_256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
