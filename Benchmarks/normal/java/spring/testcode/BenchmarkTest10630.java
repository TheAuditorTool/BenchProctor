// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10630 {

    @GetMapping("/BenchmarkTest10630")
    public void BenchmarkTest10630(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "s3cr3t_key_test_xyz";
        String data = "[%s]".formatted(secretValue);
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
