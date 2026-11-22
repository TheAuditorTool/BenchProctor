# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import MD4
import json


def BenchmarkTest00026(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = '%s' % (graphql_var,)
    digest = MD4.new(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
