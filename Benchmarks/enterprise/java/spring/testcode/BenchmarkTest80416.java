// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80416 {

    @GetMapping("/BenchmarkTest80416")
    public void BenchmarkTest80416(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "AKIAIOSFODNN7EXAMPLE";
        String data = secretValue.isEmpty() ? "default" : secretValue;
        String hardcodedPassword = "P@ssw0rd_corp_2024";
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", hardcodedPassword)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
