// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;

@RestController
class AuditBundle {

    private static final class EntityManagers {
        static final jakarta.persistence.EntityManagerFactory FACTORY = jakarta.persistence.Persistence.createEntityManagerFactory("appPU");
    }
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

    @GetMapping("/AuditBundle")
    public void auditBundle(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = java.util.Optional.ofNullable(System.getenv("TELEMETRY_INPUT_0024")).orElse("");
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : summary.split(",")) { tokens.add(token.trim()); }
        String cohort = String.join(",", tokens);
        jakarta.persistence.EntityManager em = EntityManagers.FACTORY.createEntityManager();
        em.createQuery("FROM User WHERE id = :id", Object.class)
            .setParameter("id", cohort)
            .getResultList();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
