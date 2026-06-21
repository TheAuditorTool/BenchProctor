// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest41093 {

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
    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest41093")
    public void BenchmarkTest41093(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        holder.set(refererValue);
        String data = holder.get();
        java.net.URI parsed = java.net.URI.create(data);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.endsWith(".svc.local") && !parsedHost.endsWith(".acmecdn.net")) {
            response.sendError(403, "forbidden host"); return;
        }
        String targetUrl = data;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(targetUrl)).GET().build();
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
