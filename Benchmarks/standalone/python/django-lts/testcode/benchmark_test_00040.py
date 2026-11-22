# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import MD4
import json


def BenchmarkTest00040(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    digest = MD4.new(str(json_value).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
