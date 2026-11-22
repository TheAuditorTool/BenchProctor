// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <regex>

struct sqlite3; struct sqlite3_stmt;
extern "C" int sqlite3_open(const char *, sqlite3 **);
extern "C" int sqlite3_exec(sqlite3 *, const char *, int (*)(void *, int, char **, char **), void *, char **);
extern "C" int sqlite3_prepare_v2(sqlite3 *, const char *, int, sqlite3_stmt **, const char **);
extern "C" int sqlite3_bind_text(sqlite3_stmt *, int, const char *, int, void (*)(void *));
extern "C" int sqlite3_step(sqlite3_stmt *);
extern "C" int sqlite3_finalize(sqlite3_stmt *);
extern "C" int sqlite3_get_table(sqlite3 *, const char *, char ***, int *, int *, char **); extern "C" void sqlite3_free_table(char **);

void benchmark_test_00051(int, char **)
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
    static const std::regex _re("^[a-zA-Z0-9_.#\\-]+$");
    std::string arg = std::regex_match(user_input, _re) ? user_input : std::string("default");
    sqlite3 *_db = nullptr;
    sqlite3_open("app.db", &_db);
    std::string _sqlq = std::string("SELECT name, email FROM users WHERE name = '") + arg + "'";
    char **_rows = nullptr;
    int _nrow = 0, _ncol = 0;
    sqlite3_get_table(_db, _sqlq.c_str(), &_rows, &_nrow, &_ncol, nullptr);
    for (int _r = 1; _r <= _nrow; ++_r) std::cout << _rows[_r * _ncol + 1] << std::endl;
    sqlite3_free_table(_rows);
}
