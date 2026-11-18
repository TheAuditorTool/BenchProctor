// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00709 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    private static java.sql.Connection connection;
    static {
        try {
            connection = java.sql.DriverManager.getConnection("jdbc:h2:mem:bench;DB_CLOSE_DELAY=-1;NON_KEYWORDS=VALUE", "sa", "");
            try (var stmt = connection.createStatement()) {
                stmt.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR DEFAULT '' NOT NULL, role VARCHAR DEFAULT 'user' NOT NULL, bio VARCHAR DEFAULT '' NOT NULL, email VARCHAR DEFAULT '' NOT NULL, password VARCHAR DEFAULT '' NOT NULL, token_hash VARCHAR DEFAULT '' NOT NULL, locked INTEGER DEFAULT 0 NOT NULL)");
                stmt.execute("MERGE INTO users t USING (VALUES (1, 'alice', 'user', 'Enjoys hiking', 'alice@example.com'), (2, 'bob', 'user', 'Coffee enthusiast', 'bob@example.com'), (3, 'admin', 'admin', 'Site administrator', 'admin@example.com')) s(id, name, role, bio, email) ON t.id = s.id WHEN NOT MATCHED THEN INSERT (id, name, role, bio, email) VALUES (s.id, s.name, s.role, s.bio, s.email)");
                stmt.execute("CREATE TABLE IF NOT EXISTS kv_cache (k VARCHAR PRIMARY KEY, value VARCHAR DEFAULT '' NOT NULL)");
                stmt.execute("MERGE INTO kv_cache t USING (VALUES ('user_data', 'cached_value')) s(k, value) ON t.k = s.k WHEN NOT MATCHED THEN INSERT (k, value) VALUES (s.k, s.value)");
            }
        } catch (java.sql.SQLException ignored) {}
    }
    private static String dbReadColumn(String sql) {
        try (var stmt = connection.createStatement();
             var rs = stmt.executeQuery(sql)) {
            return rs.next() ? rs.getString(1) : "";
        } catch (java.sql.SQLException e) {
            return "";
        }
    }

    @GetMapping("/BenchmarkTest00709")
    public void BenchmarkTest00709(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cachedValue = java.util.Optional.ofNullable(dbReadColumn("SELECT value FROM kv_cache WHERE k = 'user_data' LIMIT 1")).orElse("");
        String data;
        try { data = new String(java.util.Base64.getDecoder().decode(cachedValue), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { data = cachedValue; }
        try (Statement stmt = connection.createStatement()) {
            stmt.executeQuery("SELECT * FROM users WHERE id = '" + data + "'");
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
