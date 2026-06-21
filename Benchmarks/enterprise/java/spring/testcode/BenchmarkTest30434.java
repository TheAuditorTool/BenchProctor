// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest30434 {

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

    @PostMapping(path="/BenchmarkTest30434", consumes="multipart/form-data")
    public void BenchmarkTest30434(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(uploadName);
        String data = wrapper.toString();
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            try (PreparedStatement ps = connection.prepareStatement("SELECT * FROM users WHERE id = ?")) {
                ps.setString(1, data);
                try (ResultSet rs = ps.executeQuery()) { /* result consumed */ }
            }
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
