# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest53155(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not graphql_var.lower().endswith(allowed_ext):
        return JsonResponse({'error': 'invalid file type'}, status=400)
    entry_file = os.path.basename(graphql_var)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
