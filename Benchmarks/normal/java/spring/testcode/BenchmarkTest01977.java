// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01977 {

    @GetMapping("/BenchmarkTest01977")
    public void BenchmarkTest01977(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "s3cr3t_key_test_xyz";
        StringBuilder bundle = new StringBuilder();
        bundle.append(secretValue);
        String data = bundle.toString();
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
