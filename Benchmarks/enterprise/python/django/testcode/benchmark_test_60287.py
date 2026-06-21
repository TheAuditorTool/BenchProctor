# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def BenchmarkTest60287(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
