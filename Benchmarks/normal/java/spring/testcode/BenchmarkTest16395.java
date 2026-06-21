// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16395 {

    @GetMapping("/BenchmarkTest16395")
    public void BenchmarkTest16395(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "s3cr3t_key_test_xyz";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(secretValue, "query");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
