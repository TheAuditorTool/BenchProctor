# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def annotate_promotion(request):
    headline = request.GET.get('id', '')
    parts = []
    for token in str(headline).split(','):
        parts.append(token.strip())
    backorder = ','.join(parts)
    subprocess.run(['echo', backorder], shell=False)
    return JsonResponse({"saved": True})
