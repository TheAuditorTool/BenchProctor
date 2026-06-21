// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest70889 {

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

    @GetMapping("/BenchmarkTest70889")
    public void BenchmarkTest70889(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        byte[] hexBytes = new byte[cookieValue.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(cookieValue.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String data = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        jakarta.persistence.EntityManager em = (jakarta.persistence.EntityManager) request.getAttribute("em");
        if (em == null) { response.sendError(503, "no entity manager"); return; }
        em.createQuery("FROM User WHERE name = :name", Object.class)
            .setParameter("name", data)
            .getResultList();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
