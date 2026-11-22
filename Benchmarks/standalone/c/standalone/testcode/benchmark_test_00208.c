// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

struct c_plan { const char *name; int limit; };
static int c_plan_cmp(const void *_key, const void *_entry) { return strcmp((const char *)_key, ((const struct c_plan *)_entry)->name); }

void benchmark_test_00208(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    FILE *_src_fp = fopen("/etc/app/config", "r");
    if (_src_fp != NULL) {
        if (fgets(user_input_buf, sizeof(user_input_buf), _src_fp) == NULL) user_input_buf[0] = '\0';
        fclose(_src_fp);
    }
    const char *user_input = user_input_buf;
    static const struct c_plan _plans[] = { { "basic", 10 }, { "enterprise", 1000 }, { "pro", 100 } };
    const struct c_plan *_plan = bsearch(user_input, _plans, sizeof(_plans) / sizeof(_plans[0]), sizeof(_plans[0]), c_plan_cmp);
    int _limit = _plan->limit;
    printf("limit %d\n", _limit);
}
