// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06350 {

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

    @GetMapping("/BenchmarkTest06350/{pathId}")
    public void BenchmarkTest06350(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{pathValue});
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
