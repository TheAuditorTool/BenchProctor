// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06336 {

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

    @PostMapping(path="/BenchmarkTest06336", consumes="multipart/form-data")
    public void BenchmarkTest06336(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String prefix = multipartValue.length() > 0 ? multipartValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = multipartValue.toLowerCase(); break;
            case "f": data = multipartValue.toUpperCase(); break;
            default: data = multipartValue.strip(); break;
        }
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
