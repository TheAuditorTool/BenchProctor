// SPDX-License-Identifier: Apache-2.0
package com.example.changelogbuilder;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class RotateLedger {

    @org.springframework.beans.factory.annotation.Autowired
    private javax.sql.DataSource dataSource;

    private java.sql.Connection connection;

    @jakarta.annotation.PostConstruct
    void initSchema() {
        try {
            connection = dataSource.getConnection();
            if (connection.getMetaData().getURL().startsWith("jdbc:h2:")) {
                try (var stmt = connection.createStatement()) {
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

    @GetMapping("/RotateLedger")
    public void rotateLedger(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = java.util.Optional.ofNullable(dbReadColumn("SELECT body FROM mq_messages ORDER BY id DESC LIMIT 1")).orElse("");
        String wording;
        if (footnote.length() > 256) { wording = footnote.substring(0, 256); }
        else { wording = footnote; }
        byte[] serBytes = java.util.Base64.getDecoder().decode(wording);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
