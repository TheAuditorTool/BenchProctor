// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>

struct sqlite3; struct sqlite3_stmt;
extern "C" int sqlite3_open(const char *, sqlite3 **);
extern "C" int sqlite3_exec(sqlite3 *, const char *, int (*)(void *, int, char **, char **), void *, char **);
extern "C" int sqlite3_prepare_v2(sqlite3 *, const char *, int, sqlite3_stmt **, const char **);
extern "C" int sqlite3_bind_text(sqlite3_stmt *, int, const char *, int, void (*)(void *));
extern "C" int sqlite3_step(sqlite3_stmt *);
extern "C" int sqlite3_finalize(sqlite3_stmt *);

void benchmark_test_00507(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    sqlite3 *_db = nullptr;
    sqlite3_open("app.db", &_db);
    sqlite3_stmt *_st = nullptr;
    sqlite3_prepare_v2(_db, "SELECT * FROM users WHERE name = ?", -1, &_st, nullptr);
    sqlite3_bind_text(_st, 1, data.c_str(), -1, nullptr);
    sqlite3_step(_st);
    sqlite3_finalize(_st);
}
