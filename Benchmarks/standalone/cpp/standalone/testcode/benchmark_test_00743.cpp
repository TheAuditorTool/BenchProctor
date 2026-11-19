// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <unistd.h>

struct sqlite3; struct sqlite3_stmt;
extern "C" int sqlite3_open(const char *, sqlite3 **);
extern "C" int sqlite3_exec(sqlite3 *, const char *, int (*)(void *, int, char **, char **), void *, char **);
extern "C" int sqlite3_prepare_v2(sqlite3 *, const char *, int, sqlite3_stmt **, const char **);
extern "C" int sqlite3_bind_text(sqlite3_stmt *, int, const char *, int, void (*)(void *));
extern "C" int sqlite3_step(sqlite3_stmt *);
extern "C" int sqlite3_finalize(sqlite3_stmt *);

void benchmark_test_00743(int, char **)
{
    std::string user_input;
    if (FILE *_fp = std::fopen("/etc/app/config", "r")) {
        char _b[256];
        if (std::fgets(_b, sizeof(_b), _fp)) {
            _b[std::strcspn(_b, "\n")] = 0;
            user_input = _b;
        }
        std::fclose(_fp);
    }
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    sqlite3 *_db = nullptr;
    sqlite3_open("app.db", &_db);
    std::string _sqlq = std::string("SELECT * FROM users WHERE name = '") + data + "'";
    sqlite3_exec(_db, _sqlq.c_str(), nullptr, nullptr, nullptr);
}
