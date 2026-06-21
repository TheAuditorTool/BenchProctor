# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def BenchmarkTest01520(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', graphql_var):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = graphql_var
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
