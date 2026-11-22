# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def validate_policy(request):
    synopsis = request.GET.get('id', '')
    parts = []
    for token in str(synopsis).split(','):
        parts.append(token.strip())
    byline = ','.join(parts)
    subprocess.run(['echo', byline], shell=False)
    return JsonResponse({"saved": True})
