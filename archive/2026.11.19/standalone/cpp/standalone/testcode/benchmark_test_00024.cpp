// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>

struct sqlite3; struct sqlite3_stmt;
extern "C" int sqlite3_open(const char *, sqlite3 **);
extern "C" int sqlite3_exec(sqlite3 *, const char *, int (*)(void *, int, char **, char **), void *, char **);
extern "C" int sqlite3_prepare_v2(sqlite3 *, const char *, int, sqlite3_stmt **, const char **);
extern "C" int sqlite3_bind_text(sqlite3_stmt *, int, const char *, int, void (*)(void *));
extern "C" int sqlite3_step(sqlite3_stmt *);
extern "C" int sqlite3_finalize(sqlite3_stmt *);
static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00024(int, char **)
{
    std::string user_input;
    if (const char *user_input_cl = std::getenv("CONTENT_LENGTH")) {
        long user_input_n = std::strtol(user_input_cl, nullptr, 10);
        if (user_input_n > 0 && user_input_n < 1048576) {
            user_input.resize((size_t)user_input_n);
            std::cin.read(&user_input[0], user_input_n);
            user_input.resize((size_t)std::cin.gcount());
        }
    }
    std::string data = cpp_own(user_input);
    sqlite3 *_db = nullptr;
    sqlite3_open("app.db", &_db);
    std::string _sqlq = std::string("SELECT * FROM users WHERE name = '") + data + "'";
    sqlite3_exec(_db, _sqlq.c_str(), nullptr, nullptr, nullptr);
}
