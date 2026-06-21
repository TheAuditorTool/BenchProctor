// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12622 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest12622")
    public void BenchmarkTest12622(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "AKIAIOSFODNN7EXAMPLE";
        String data = trimEnds(secretValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", processed)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
