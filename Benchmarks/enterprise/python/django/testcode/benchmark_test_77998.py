# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def BenchmarkTest77998(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
