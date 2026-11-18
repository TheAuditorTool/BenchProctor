# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def enrich_policy(request):
    remark = request.META.get('HTTP_REFERER', '')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    inquiry = ','.join(parts)
    subprocess.Popen('echo ' + str(inquiry), shell=True).wait()
    return JsonResponse({"saved": True})
