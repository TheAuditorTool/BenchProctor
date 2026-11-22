# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import numpy as np


def BenchmarkTest00178(request, path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    quantity = int(str(data))
    total_cents = np.int32(quantity) * np.int32(1999)
    return JsonResponse({'total_cents': int(total_cents)}, status=200)
