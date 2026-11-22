# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def build_checkpoint(request, path_param):
    heading = request.path.split('/')[-1]
    handshake = f'{heading!s}'
    os.unlink('/var/app/data/' + str(handshake))
    return JsonResponse({"saved": True})
