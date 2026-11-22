# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def annotate_header(request):
    headline = request.GET.get('id', '')
    parts = []
    for token in str(headline).split(','):
        parts.append(token.strip())
    disbursement = ','.join(parts)
    subprocess.run(['echo', disbursement], shell=False)
    return JsonResponse({"saved": True})
