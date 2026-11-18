# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def rotate_batch(request):
    preface = request.COOKIES.get('session_token', '')
    handshake = preface if preface else 'default'
    os.system('echo ' + str(handshake))
    return JsonResponse({"saved": True})
