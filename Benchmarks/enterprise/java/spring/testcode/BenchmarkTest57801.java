// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest57801 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

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
    private static final java.util.concurrent.atomic.AtomicReference<String> sharedRef = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping(path="/BenchmarkTest57801", consumes="application/json")
    public void BenchmarkTest57801(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        sharedRef.set(graphqlVar);
        String data = sharedRef.get();
        if (System.currentTimeMillis() > 1000000000000L) {
            jakarta.persistence.EntityManager em = (jakarta.persistence.EntityManager) request.getAttribute("em");
            if (em == null) { response.sendError(503, "no entity manager"); return; }
            em.createQuery("FROM User WHERE name = '" + data + "'", Object.class)
                .getResultList();
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
