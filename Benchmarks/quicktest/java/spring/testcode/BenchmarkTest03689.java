// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03689 {

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

    @GetMapping("/BenchmarkTest03689")
    public void BenchmarkTest03689(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "feature_flag_value";
        java.util.List<String> tokens = java.util.Arrays.asList(secretValue.split(","));
        String data = String.join(",", tokens);
        if (data == null) throw new IllegalArgumentException("input required");
        String envSecret = System.getenv("APP_SECRET");
        if (envSecret == null) throw new IllegalStateException("APP_SECRET unset");
        String storeCred = envSecret;
        String dbPass = System.getenv("DB_PASSWORD");
        DriverManager.getConnection("jdbc:postgresql://db/prod", "app", dbPass);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
