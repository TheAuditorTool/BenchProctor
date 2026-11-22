# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def load_subscription(request):
    preface = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    bulletin = normalize(preface)
    subprocess.run('echo ' + str(bulletin), shell=True)
    return JsonResponse({"saved": True})
