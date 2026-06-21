// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest63515 {

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

    @PostMapping(path="/BenchmarkTest63515", consumes="multipart/form-data")
    public void BenchmarkTest63515(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String prefix = multipartValue.length() > 0 ? multipartValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = multipartValue.toLowerCase(); break;
            case "f": data = multipartValue.toUpperCase(); break;
            default: data = multipartValue.strip(); break;
        }
        String fetched;
        try (java.sql.PreparedStatement ps = connection.prepareStatement("SELECT name FROM users WHERE id = ?")) {
            ps.setString(1, data);
            try (java.sql.ResultSet rs = ps.executeQuery()) {
                fetched = rs.next() ? rs.getString("name") : null;
            }
        }
        response.setHeader("X-Name-Length", String.valueOf(fetched.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
