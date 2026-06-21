// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest42121 {

    private static String stripWhitespace(String v) { return v.strip(); }
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

    @GetMapping("/BenchmarkTest42121")
    public void BenchmarkTest42121(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = stripWhitespace(uaValue);
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            try (Statement stmt = connection.createStatement()) {
                stmt.executeQuery("SELECT * FROM users WHERE id = " + data);
            }
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
