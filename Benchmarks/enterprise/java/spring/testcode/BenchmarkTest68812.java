// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import java.sql.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest68812 {
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
            }
        } catch (java.sql.SQLException ignored) {}
    }

    @PostMapping("/BenchmarkTest68812")
    public void BenchmarkTest68812(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        jakarta.persistence.EntityManager em = (jakarta.persistence.EntityManager) request.getAttribute("em");
        if (em == null) { response.sendError(503, "no entity manager"); return; }
        em.createQuery("FROM User WHERE name = :name", Object.class)
            .setParameter("name", jsonValue)
            .getResultList();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
