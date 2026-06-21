// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10768 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest10768")
    public void BenchmarkTest10768(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "config_secret_test_abc123";
        String data = trimEnds(secretValue);
        String hardcodedPassword = "P@ssw0rd_corp_2024";
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", hardcodedPassword)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
