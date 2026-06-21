// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest00578 {

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

    @PostMapping(path="/BenchmarkTest00578", consumes="multipart/form-data")
    public void BenchmarkTest00578(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data;
        if (uploadName.length() > 256) { data = uploadName.substring(0, 256); }
        else { data = uploadName; }
        if (request.getUserPrincipal() == null) { response.sendError(401, "unauthenticated"); return; }
        String currentUser = request.getUserPrincipal().getName();
        try (PreparedStatement ps = connection.prepareStatement("SELECT * FROM users WHERE id = ? AND name = ?")) {
            ps.setString(1, data);
            ps.setString(2, currentUser);
            try (ResultSet rs = ps.executeQuery()) { /* owner-scoped result consumed */ }
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
