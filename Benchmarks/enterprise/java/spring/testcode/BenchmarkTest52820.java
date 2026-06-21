// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest52820 {

    @GetMapping("/BenchmarkTest52820")
    public void BenchmarkTest52820(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "AKIAIOSFODNN7EXAMPLE";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(secretValue, "header");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
