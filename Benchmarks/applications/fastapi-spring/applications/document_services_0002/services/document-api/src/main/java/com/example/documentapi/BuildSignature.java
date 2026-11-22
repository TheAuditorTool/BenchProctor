// SPDX-License-Identifier: Apache-2.0
package com.example.documentapi;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@RestController
class BuildSignature {

    @org.springframework.beans.factory.annotation.Autowired
    private javax.sql.DataSource dataSource;

    private java.sql.Connection connection;

    @javax.annotation.PostConstruct
    void initSchema() {
        try {
            connection = dataSource.getConnection();
            if (connection.getMetaData().getURL().startsWith("jdbc:h2:")) {
                try (java.sql.Statement stmt = connection.createStatement()) {
                    stmt.execute("CREATE TABLE IF NOT EXISTS kv_cache (k VARCHAR PRIMARY KEY, value VARCHAR DEFAULT '' NOT NULL)");
                    stmt.execute("MERGE INTO kv_cache t USING (VALUES ('user_data', 'cached_value')) s(k, value) ON t.k = s.k WHEN NOT MATCHED THEN INSERT (k, value) VALUES (s.k, s.value)");
                }
            }
        } catch (java.sql.SQLException ignored) {}
    }
    @org.springframework.beans.factory.annotation.Autowired
    private org.springframework.jdbc.core.JdbcTemplate jdbcTemplate;

    private String dbReadColumn(String sql) {
        try {
            return java.util.Optional.ofNullable(
                jdbcTemplate.queryForObject(sql, String.class)).orElse("");
        } catch (org.springframework.dao.DataAccessException e) {
            return "";
        }
    }

    @GetMapping("/BuildSignature")
    public void buildSignature(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String wording = java.util.Optional.ofNullable(dbReadColumn("SELECT value FROM kv_cache WHERE k = 'user_data' LIMIT 1")).orElse("");
        String prefix = wording.length() > 0 ? wording.substring(0, 1).toLowerCase() : "";
        String addendum;
        switch (prefix) {
            case "h": addendum = wording.toLowerCase(); break;
            case "f": addendum = wording.toUpperCase(); break;
            default: addendum = wording.strip(); break;
        }
        java.net.URI parsed = java.net.URI.create(addendum);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { response.sendError(403); return; }
        String dossier = addendum;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(dossier)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
