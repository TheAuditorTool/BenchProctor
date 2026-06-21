// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05118 {

    @GetMapping("/BenchmarkTest05118")
    public void BenchmarkTest05118(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "app_display_name";
        String prefix = secretValue.length() > 0 ? secretValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = secretValue.toLowerCase(); break;
            case "f": data = secretValue.toUpperCase(); break;
            default: data = secretValue.strip(); break;
        }
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
