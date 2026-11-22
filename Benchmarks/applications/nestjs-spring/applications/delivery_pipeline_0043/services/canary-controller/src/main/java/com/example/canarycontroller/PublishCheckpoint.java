// SPDX-License-Identifier: Apache-2.0
package com.example.canarycontroller;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class PublishCheckpoint {

    @org.springframework.beans.factory.annotation.Autowired
    private javax.sql.DataSource dataSource;

    private java.sql.Connection connection;

    @javax.annotation.PostConstruct
    void initSchema() {
        try {
            connection = dataSource.getConnection();
            if (connection.getMetaData().getURL().startsWith("jdbc:h2:")) {
                try (java.sql.Statement stmt = connection.createStatement()) {
                    stmt.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR DEFAULT '' NOT NULL, role VARCHAR DEFAULT 'user' NOT NULL, bio VARCHAR DEFAULT '' NOT NULL, email VARCHAR DEFAULT '' NOT NULL, password VARCHAR DEFAULT '' NOT NULL, token_hash VARCHAR DEFAULT '' NOT NULL, locked INTEGER DEFAULT 0 NOT NULL)");
                    stmt.execute("MERGE INTO users t USING (VALUES (1, 'alice', 'user', 'Enjoys hiking', 'alice@example.com'), (2, 'bob', 'user', 'Coffee enthusiast', 'bob@example.com'), (3, 'admin', 'admin', 'Site administrator', 'admin@example.com')) s(id, name, role, bio, email) ON t.id = s.id WHEN NOT MATCHED THEN INSERT (id, name, role, bio, email) VALUES (s.id, s.name, s.role, s.bio, s.email)");
                }
            }
        } catch (java.sql.SQLException ignored) {}
    }

    @GetMapping("/PublishCheckpoint")
    public void publishCheckpoint(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/var/app/data.txt")))).orElse("");
        String note;
        try { note = new String(java.util.Base64.getDecoder().decode(remark), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { note = remark; }
        int parsedIntValue;
        try { parsedIntValue = Integer.parseInt(note); }
        catch (NumberFormatException e) { response.sendError(400); return; }
        String phrase = String.valueOf(parsedIntValue);
        int coercedId = Integer.parseInt(phrase);
        try (java.sql.PreparedStatement lookupStmt =
                connection.prepareStatement("SELECT id, name FROM users WHERE id = " + coercedId);
             java.sql.ResultSet lookupRows = lookupStmt.executeQuery()) {
            lookupRows.next();
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
