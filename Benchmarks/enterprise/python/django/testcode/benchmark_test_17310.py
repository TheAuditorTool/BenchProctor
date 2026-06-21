# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import pickle


def BenchmarkTest17310(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
