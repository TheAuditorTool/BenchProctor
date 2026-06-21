# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from urllib.parse import unquote


def BenchmarkTest14057(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JsonResponse({'validated': str(processed)}, status=200)
    return JsonResponse({"saved": True})
