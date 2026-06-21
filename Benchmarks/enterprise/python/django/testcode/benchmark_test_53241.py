# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def BenchmarkTest53241(request):
    multipart_value = request.POST.get('multipart_field', '')
    processed = shlex.quote(multipart_value)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
