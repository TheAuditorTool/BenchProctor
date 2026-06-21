# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def BenchmarkTest12219(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
