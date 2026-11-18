// SPDX-License-Identifier: Apache-2.0
package com.example.dashboardapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;

@RestController
class EnrichPolicy {

    @org.springframework.beans.factory.annotation.Autowired
    private javax.sql.DataSource dataSource;

    private java.sql.Connection connection;

    @jakarta.annotation.PostConstruct
    void initSchema() {
        try {
            connection = dataSource.getConnection();
            if (connection.getMetaData().getURL().startsWith("jdbc:h2:")) {
                try (var stmt = connection.createStatement()) {
                    stmt.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR DEFAULT '' NOT NULL, role VARCHAR DEFAULT 'user' NOT NULL, bio VARCHAR DEFAULT '' NOT NULL, email VARCHAR DEFAULT '' NOT NULL, password VARCHAR DEFAULT '' NOT NULL, token_hash VARCHAR DEFAULT '' NOT NULL, locked INTEGER DEFAULT 0 NOT NULL)");
                    stmt.execute("MERGE INTO users t USING (VALUES (1, 'alice', 'user', 'Enjoys hiking', 'alice@example.com'), (2, 'bob', 'user', 'Coffee enthusiast', 'bob@example.com'), (3, 'admin', 'admin', 'Site administrator', 'admin@example.com')) s(id, name, role, bio, email) ON t.id = s.id WHEN NOT MATCHED THEN INSERT (id, name, role, bio, email) VALUES (s.id, s.name, s.role, s.bio, s.email)");
                    stmt.execute("CREATE TABLE IF NOT EXISTS mq_messages (id INTEGER PRIMARY KEY, queue VARCHAR DEFAULT '' NOT NULL, body VARCHAR DEFAULT '' NOT NULL)");
                    stmt.execute("MERGE INTO mq_messages t USING (VALUES (1, 'msg-001')) s(id, body) ON t.id = s.id WHEN NOT MATCHED THEN INSERT (id, body) VALUES (s.id, s.body)");
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

    @GetMapping("/EnrichPolicy")
    public void enrichPolicy(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = java.util.Optional.ofNullable(dbReadColumn("SELECT body FROM mq_messages ORDER BY id DESC LIMIT 1")).orElse("");
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String cohort = transform.apply(headline);
        try (Statement stmt = connection.createStatement()) {
            stmt.executeQuery("SELECT * FROM users WHERE id = '" + cohort + "'");
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
