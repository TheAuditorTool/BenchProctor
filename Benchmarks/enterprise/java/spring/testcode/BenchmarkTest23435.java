// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest23435 {

    @GetMapping("/BenchmarkTest23435")
    public void BenchmarkTest23435(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(originValue);
        String data = normalizer.apply(originValue);
        java.security.MessageDigest md = java.security.MessageDigest.getInstance("SHA-256");
        String hashedCred = java.util.Base64.getEncoder().encodeToString(md.digest(data.getBytes(java.nio.charset.StandardCharsets.UTF_8)));
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", hashedCred)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
