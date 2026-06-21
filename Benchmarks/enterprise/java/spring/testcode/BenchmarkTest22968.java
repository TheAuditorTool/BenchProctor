// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22968 {

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
    private static final java.util.concurrent.atomic.AtomicReference<String> ref = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping("/BenchmarkTest22968")
    public void BenchmarkTest22968(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        ref.set(commentValue);
        String data = ref.get();
        if (!authCheck(request.getSession().getAttribute("role"), data)) {
            response.sendError(403, "forbidden");
            return;
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
