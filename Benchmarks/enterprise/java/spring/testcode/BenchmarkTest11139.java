// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest11139 {

    private static java.sql.Connection connection;
    static {
        try {
            connection = java.sql.DriverManager.getConnection("jdbc:h2:mem:bench;DB_CLOSE_DELAY=-1", "sa", "");
            try (var stmt = connection.createStatement()) {
                stmt.execute("CREATE TABLE IF NOT EXISTS users (id INT, name VARCHAR(64))");
                stmt.execute("INSERT INTO users (id, name) VALUES (1, 'alice')");
            }
        } catch (java.sql.SQLException ignored) {}
    }
    private static final java.util.concurrent.atomic.AtomicReference<String> sharedRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest11139")
    public void BenchmarkTest11139(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "config_secret_test_abc123";
        sharedRef.set(secretValue);
        String data = sharedRef.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        DriverManager.getConnection("jdbc:postgresql://db/prod", "app", processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
