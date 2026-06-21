// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80740 {

    private static java.sql.Connection connection;
    static {
        try {
            connection = java.sql.DriverManager.getConnection("jdbc:h2:mem:bench;DB_CLOSE_DELAY=-1", "sa", "");
            try (var stmt = connection.createStatement()) {
                stmt.execute("CREATE TABLE IF NOT EXISTS users (id INT, name VARCHAR(64))");
                stmt.execute("INSERT INTO users (id, name) VALUES (1, 'alice')");
                stmt.execute("CREATE TABLE IF NOT EXISTS logs (id INT AUTO_INCREMENT, data VARCHAR(1024))");
                stmt.execute("INSERT INTO logs (data) VALUES ('seed-entry')");
            }
        } catch (java.sql.SQLException ignored) {}
    }
    private static boolean authCheck(Object v, Object t) { return v != null && v.equals(t); }

    @GetMapping("/BenchmarkTest80740")
    public void BenchmarkTest80740(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        org.springframework.security.core.Authentication auth = org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication();
        if (auth == null || auth.getAuthorities().stream().noneMatch(a -> a.getAuthority().equals("ROLE_ADMIN"))) {
            response.sendError(403, "forbidden"); return;
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
