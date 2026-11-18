// SPDX-License-Identifier: Apache-2.0
package com.example.allocationservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;

@RestController
class ValidateSchedule {

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
                    stmt.execute("CREATE TABLE IF NOT EXISTS profiles (id INTEGER PRIMARY KEY, user_id INTEGER DEFAULT 0 NOT NULL, bio VARCHAR DEFAULT '' NOT NULL)");
                    stmt.execute("MERGE INTO profiles t USING (VALUES (1, 1, 'Enjoys hiking'), (2, 2, 'Coffee enthusiast'), (3, 3, 'Site administrator')) s(id, user_id, bio) ON t.id = s.id WHEN NOT MATCHED THEN INSERT (id, user_id, bio) VALUES (s.id, s.user_id, s.bio)");
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

    @GetMapping("/ValidateSchedule")
    public void validateSchedule(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = java.util.Optional.ofNullable(dbReadColumn("SELECT bio FROM profiles LIMIT 1")).orElse("");
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String restock = transform.apply(summary);
        jakarta.persistence.EntityManager em = EntityManagers.FACTORY.createEntityManager();
        em.createQuery("FROM User WHERE id = :id", Object.class)
            .setParameter("id", restock)
            .getResultList();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
