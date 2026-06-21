// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest41141 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GetMapping("/BenchmarkTest41141")
    public void BenchmarkTest41141(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "AKIAIOSFODNN7EXAMPLE";
        String data = stripCRLF(secretValue);
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
