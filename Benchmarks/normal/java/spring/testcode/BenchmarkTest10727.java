// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10727 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GetMapping("/BenchmarkTest10727")
    public void BenchmarkTest10727(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "default_setting_value";
        String data = stripCRLF(secretValue);
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
