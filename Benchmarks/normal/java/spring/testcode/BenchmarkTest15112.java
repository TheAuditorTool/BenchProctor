// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15112 {

    @GetMapping("/BenchmarkTest15112")
    public void BenchmarkTest15112(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "config_secret_test_abc123";
        java.util.List<String> tokens = java.util.Arrays.asList(secretValue.split(","));
        String data = String.join(",", tokens);
        String hardcodedPassword = "P@ssw0rd_corp_2024";
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", hardcodedPassword)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
