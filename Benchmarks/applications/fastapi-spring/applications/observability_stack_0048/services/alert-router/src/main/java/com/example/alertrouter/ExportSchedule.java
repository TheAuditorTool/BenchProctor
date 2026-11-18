// SPDX-License-Identifier: Apache-2.0
package com.example.alertrouter;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;

@RestController
class ExportSchedule {

    private static String normalize(String v) { return v.strip(); }
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
                }
            }
        } catch (java.sql.SQLException ignored) {}
    }

    @GetMapping("/ExportSchedule")
    public void exportSchedule(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/var/app/data.txt")))).orElse("");
        String gauge = normalize(excerpt);
        String sortKey = gauge.replaceAll("[^a-zA-Z0-9_]", "");
        try (Statement stmt = connection.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT * FROM users ORDER BY " + sortKey)) {
            rs.next();
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
