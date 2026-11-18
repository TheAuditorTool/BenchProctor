# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def render_ticket(request):
    phrase = request.GET.get('id', '')
    inquiry, _sep, _rest = str(phrase).partition('\x00')
    os.system('echo ' + str(inquiry))
    return JsonResponse({"saved": True})
