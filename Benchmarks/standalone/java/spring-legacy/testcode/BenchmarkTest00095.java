// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00095 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    private static java.sql.Connection connection;
    static {
        try {
            connection = java.sql.DriverManager.getConnection("jdbc:h2:mem:bench;DB_CLOSE_DELAY=-1;NON_KEYWORDS=VALUE", "sa", "");
            try (java.sql.Statement stmt = connection.createStatement()) {
                stmt.execute("CREATE TABLE IF NOT EXISTS profiles (id INTEGER PRIMARY KEY, user_id INTEGER DEFAULT 0 NOT NULL, bio VARCHAR DEFAULT '' NOT NULL)");
                stmt.execute("MERGE INTO profiles t USING (VALUES (1, 1, 'Enjoys hiking'), (2, 2, 'Coffee enthusiast'), (3, 3, 'Site administrator')) s(id, user_id, bio) ON t.id = s.id WHEN NOT MATCHED THEN INSERT (id, user_id, bio) VALUES (s.id, s.user_id, s.bio)");
            }
        } catch (java.sql.SQLException ignored) {}
    }
    private static String dbReadColumn(String sql) {
        try (java.sql.Statement stmt = connection.createStatement();
             java.sql.ResultSet rs = stmt.executeQuery(sql)) {
            return rs.next() ? rs.getString(1) : "";
        } catch (java.sql.SQLException e) {
            return "";
        }
    }

    @GetMapping("/BenchmarkTest00095")
    public void BenchmarkTest00095(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String profileBio = java.util.Optional.ofNullable(dbReadColumn("SELECT bio FROM profiles LIMIT 1")).orElse("");
        String data = String.format("%s", profileBio);
        Files.delete(Paths.get("/var/app/data/" + data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
