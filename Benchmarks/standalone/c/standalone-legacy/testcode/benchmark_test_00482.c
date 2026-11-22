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
static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00482(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    const char *data = c_passthrough(user_input);
    static const struct c_plan _plans[] = { { "basic", 10 }, { "enterprise", 1000 }, { "pro", 100 } };
    const struct c_plan *_plan = bsearch(data, _plans, sizeof(_plans) / sizeof(_plans[0]), sizeof(_plans[0]), c_plan_cmp);
    int _limit = _plan->limit;
    printf("limit %d\n", _limit);
}
