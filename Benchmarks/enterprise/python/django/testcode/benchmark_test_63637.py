# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import subprocess


def coalesce_blank(value):
    return value or ''

def BenchmarkTest63637(request):
    user_id = request.GET.get('id', '')
    data = coalesce_blank(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
