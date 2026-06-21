// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02869 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

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

    @PostMapping("/BenchmarkTest02869")
    public void BenchmarkTest02869(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        String prefix = jsonValue.length() > 0 ? jsonValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = jsonValue.toLowerCase(); break;
            case "f": data = jsonValue.toUpperCase(); break;
            default: data = jsonValue.strip(); break;
        }
        if (!authCheck(request.getSession().getAttribute("role"), data)) {
            response.sendError(403, "forbidden");
            return;
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
