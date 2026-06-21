// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest07941 {

    @GetMapping("/BenchmarkTest07941")
    public void BenchmarkTest07941(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "feature_flag_value";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(secretValue, "cookie");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        if (data == null) throw new IllegalArgumentException("input required");
        String envSecret = System.getenv("APP_SECRET");
        if (envSecret == null) throw new IllegalStateException("APP_SECRET unset");
        String storeCred = envSecret;
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", storeCred)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
