// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

struct pg_conn; typedef struct pg_conn PGconn;
struct pg_result; typedef struct pg_result PGresult;
extern "C" PGconn *PQsetdbLogin(const char *, const char *, const char *, const char *, const char *, const char *, const char *);
extern "C" int PQstatus(const PGconn *);
extern "C" void PQfinish(PGconn *);
extern "C" PGresult *PQexec(PGconn *, const char *);
extern "C" PGresult *PQexecParams(PGconn *, const char *, int, const unsigned int *, const char *const *, const int *, const int *, int);
extern "C" void PQclear(PGresult *);

void benchmark_test_00438(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_COOKIE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    PGconn *_pgc = PQsetdbLogin("db.internal", "5432", nullptr, nullptr, "appdb", "app", "");
    const char *_pgvals[1] = { data.c_str() };
    PGresult *_pgr = PQexecParams(_pgc, "SELECT * FROM users WHERE name = $1", 1, nullptr, _pgvals, nullptr, nullptr, 0);
    PQclear(_pgr);
    PQfinish(_pgc);
}
