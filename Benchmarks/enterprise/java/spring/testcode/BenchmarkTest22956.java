// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22956 {

    @GetMapping("/BenchmarkTest22956")
    public void BenchmarkTest22956(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "s3cr3t_key_test_xyz";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(secretValue, "header");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
