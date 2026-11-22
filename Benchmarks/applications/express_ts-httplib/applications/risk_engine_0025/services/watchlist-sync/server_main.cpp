#include <iostream>
#include <string>
#include <unordered_map>
#include <functional>
#include <vector>
#include <utility>
#include <cstdlib>

namespace httplib {
struct Request {
    std::string get_param_value(const std::string &key) const;
    std::string get_header_value(const std::string &key) const;
    std::unordered_map<std::string, std::string> path_params;
    std::string body;
};
struct Response {
    void set_content(const std::string &s, const std::string &type);
    void set_header(const std::string &key, const std::string &val);
    void set_redirect(const std::string &url, int status);
    int status;
};
struct Result {};
struct Client {
    Client(const std::string &host, int port);
    Result Post(const std::string &path, const std::string &body, const std::string &content_type);
};
struct Server {
    typedef std::function<void(const Request &, Response &)> Handler;
    void Get(const std::string &pattern, Handler handler);
    void Post(const std::string &pattern, Handler handler);
    bool listen(const std::string &host, int port);
    std::vector<std::pair<std::string, Handler>> routes_;
};
}

void sync_watchlist(const httplib::Request &, httplib::Response &);
void reconcile_decision(const httplib::Request &, httplib::Response &);
void merge_rule(const httplib::Request &, httplib::Response &);
void reconcile_checkpoint(const httplib::Request &, httplib::Response &);
void build_ledger(const httplib::Request &, httplib::Response &);
void collect_header(const httplib::Request &, httplib::Response &);
void export_rule(const httplib::Request &, httplib::Response &);
void fetch_bundle(const httplib::Request &, httplib::Response &);

int main()
{
    httplib::Server svr;
    svr.Get("/health", [](const httplib::Request &, httplib::Response &res) { res.set_content("ok", "text/plain"); });
    svr.Post("/sync_watchlist", &sync_watchlist);
    svr.Post("/reconcile_decision", &reconcile_decision);
    svr.Post("/merge_rule", &merge_rule);
    svr.Post("/reconcile_checkpoint", &reconcile_checkpoint);
    svr.Post("/build_ledger", &build_ledger);
    svr.Post("/collect_header", &collect_header);
    svr.Post("/export_rule", &export_rule);
    svr.Post("/fetch_bundle", &fetch_bundle);
    const char *_port_env = std::getenv("PORT");
    int _port = _port_env ? std::atoi(_port_env) : 8080;
    svr.listen("0.0.0.0", _port);
    return 0;
}
