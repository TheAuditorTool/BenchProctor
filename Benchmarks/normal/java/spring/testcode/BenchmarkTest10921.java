// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10921 {

    @GetMapping("/BenchmarkTest10921")
    public void BenchmarkTest10921(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "AKIAIOSFODNN7EXAMPLE";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(secretValue, "json");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
