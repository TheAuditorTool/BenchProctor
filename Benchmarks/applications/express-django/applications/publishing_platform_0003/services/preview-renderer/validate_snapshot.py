# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def validate_snapshot(request):
    heading = request.META.get('HTTP_AUTHORIZATION', '')
    addendum, _sep, _rest = str(heading).partition('\x00')
    os.system('echo ' + str(addendum))
    return JsonResponse({"saved": True})
