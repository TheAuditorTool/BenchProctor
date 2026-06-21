// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest57110 {

    @GetMapping("/BenchmarkTest57110")
    public void BenchmarkTest57110(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "feature_flag_value";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(secretValue, "body");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
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
