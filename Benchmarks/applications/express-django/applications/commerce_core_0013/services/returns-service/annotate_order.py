# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def annotate_order(request):
    wording = request.META.get('HTTP_USER_AGENT', '')
    backorder = (lambda v: v.strip())(wording)
    subprocess.run('echo ' + str(backorder), shell=True)
    return JsonResponse({"saved": True})
