# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def compact_report(request):
    caption = request.GET.get('id', '')
    parts = []
    for token in str(caption).split(','):
        parts.append(token.strip())
    synopsis = ','.join(parts)
    subprocess.run(['echo', synopsis], shell=False)
    return JsonResponse({"saved": True})
