# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def load_window(request):
    summary = request.GET.get('id', '')
    cohort, _sep, _rest = str(summary).partition('\x00')
    os.system('echo ' + str(cohort))
    return JsonResponse({"saved": True})
