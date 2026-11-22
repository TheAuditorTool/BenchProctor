# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponseRedirect


def BenchmarkTest00019(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id!s}'
    return HttpResponseRedirect(str(data))
