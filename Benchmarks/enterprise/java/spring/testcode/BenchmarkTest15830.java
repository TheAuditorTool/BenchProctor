// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15830 {

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

    @GetMapping("/BenchmarkTest15830")
    public void BenchmarkTest15830(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String prefix = cookieValue.length() > 0 ? cookieValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = cookieValue.toLowerCase(); break;
            case "f": data = cookieValue.toUpperCase(); break;
            default: data = cookieValue.strip(); break;
        }
        String fetched;
        try (java.sql.PreparedStatement ps = connection.prepareStatement("SELECT name FROM users WHERE id = ?")) {
            ps.setString(1, data);
            try (java.sql.ResultSet rs = ps.executeQuery()) {
                fetched = rs.next() ? rs.getString("name") : null;
            }
        }
        if (fetched == null) { response.sendError(404); return; }
        response.setHeader("X-Name-Length", String.valueOf(fetched.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
