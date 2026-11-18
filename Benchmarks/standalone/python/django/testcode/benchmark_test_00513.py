# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def BenchmarkTest00513(request):
    upload_name = request.FILES['upload'].name
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
