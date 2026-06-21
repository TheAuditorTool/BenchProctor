// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60389 {

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
    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest60389")
    public void BenchmarkTest60389(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        holder.set(hostValue);
        String data = holder.get();
        if (System.currentTimeMillis() > 1000000000000L) {
            try (PreparedStatement ps = connection.prepareStatement("SELECT * FROM users WHERE id = ?")) {
                ps.setString(1, data);
                try (ResultSet rs = ps.executeQuery()) { /* result consumed */ }
            }
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
