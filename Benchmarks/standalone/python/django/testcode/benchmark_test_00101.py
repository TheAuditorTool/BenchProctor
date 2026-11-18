# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect


def BenchmarkTest00101(request):
    field_value = request.POST.get('field', '')
    data = '%s' % (field_value,)
    return redirect(str(data))
