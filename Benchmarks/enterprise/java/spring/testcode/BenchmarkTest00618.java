// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest00618 {

    private static String normalize(String v) { return v.strip(); }
    private static java.sql.Connection connection;
    static {
        try {
            connection = java.sql.DriverManager.getConnection("jdbc:h2:mem:bench;DB_CLOSE_DELAY=-1", "sa", "");
            try (var stmt = connection.createStatement()) {
                stmt.execute("CREATE TABLE IF NOT EXISTS feed (id INT AUTO_INCREMENT, data VARCHAR(2048))");
                stmt.execute("INSERT INTO feed (data) VALUES ('seed-feed')");
            }
        } catch (java.sql.SQLException ignored) {}
    }

    @PostMapping(path="/BenchmarkTest00618", consumes="multipart/form-data")
    public void BenchmarkTest00618(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data = normalize(uploadName);
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(data)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            try (java.sql.PreparedStatement ps = connection.prepareStatement("INSERT INTO feed (data) VALUES (?)")) {
                ps.setString(1, httpResp.body());
                ps.executeUpdate();
            }
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
