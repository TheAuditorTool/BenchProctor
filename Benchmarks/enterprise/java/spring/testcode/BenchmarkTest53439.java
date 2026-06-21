// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest53439 {

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

    @GetMapping("/BenchmarkTest53439")
    public void BenchmarkTest53439(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(hostValue, "request");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        if (request.getUserPrincipal() == null) { response.sendError(401, "unauthenticated"); return; }
        String currentUser = request.getUserPrincipal().getName();
        try (PreparedStatement ps = connection.prepareStatement("SELECT * FROM users WHERE id = ? AND name = ?")) {
            ps.setString(1, data);
            ps.setString(2, currentUser);
            try (ResultSet rs = ps.executeQuery()) { /* owner-scoped result consumed */ }
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
