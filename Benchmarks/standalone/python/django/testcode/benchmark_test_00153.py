# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from urllib.parse import unquote


def BenchmarkTest00153(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
