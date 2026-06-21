// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest34866 {

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
    private static String dbReadColumn(String sql) {
        try (var stmt = connection.createStatement();
             var rs = stmt.executeQuery(sql)) {
            return rs.next() ? rs.getString(1) : "";
        } catch (java.sql.SQLException e) {
            return "";
        }
    }

    @GetMapping("/BenchmarkTest34866")
    public void BenchmarkTest34866(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userName = java.util.Optional.ofNullable(dbReadColumn("SELECT name FROM users LIMIT 1")).orElse("");
        byte[] hexBytes = new byte[userName.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(userName.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String data = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        try { Integer.parseInt(data); }
        catch (NumberFormatException e) { response.sendError(400); return; }
        String parsedId = data;
        jakarta.persistence.EntityManager em = (jakarta.persistence.EntityManager) request.getAttribute("em");
        if (em == null) { response.sendError(503, "no entity manager"); return; }
        em.createQuery("FROM User WHERE name = '" + parsedId + "'", Object.class)
            .getResultList();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
