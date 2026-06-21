# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest48553(request):
    user_id = request.GET.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
