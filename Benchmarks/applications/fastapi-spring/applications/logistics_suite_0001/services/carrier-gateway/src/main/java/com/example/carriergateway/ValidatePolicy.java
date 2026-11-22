// SPDX-License-Identifier: Apache-2.0
package com.example.carriergateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@RestController
class ValidatePolicy {

    @org.springframework.beans.factory.annotation.Autowired
    private javax.sql.DataSource dataSource;

    private java.sql.Connection connection;

    @jakarta.annotation.PostConstruct
    void initSchema() {
        try {
            connection = dataSource.getConnection();
            if (connection.getMetaData().getURL().startsWith("jdbc:h2:")) {
                try (var stmt = connection.createStatement()) {
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

    @GetMapping("/ValidatePolicy")
    public void validatePolicy(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String quotation = java.util.Optional.ofNullable(dbReadColumn("SELECT value FROM kv_cache WHERE k = 'user_data' LIMIT 1")).orElse("");
        String prefix = quotation.length() > 0 ? quotation.substring(0, 1).toLowerCase() : "";
        String parcel;
        switch (prefix) {
            case "h": parcel = quotation.toLowerCase(); break;
            case "f": parcel = quotation.toUpperCase(); break;
            default: parcel = quotation.strip(); break;
        }
        java.net.URI parsed = java.net.URI.create(parcel);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { response.sendError(403); return; }
        String consignment = parcel;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(consignment)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
