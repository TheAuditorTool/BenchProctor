// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest83338 {

    @GetMapping("/BenchmarkTest83338")
    public void BenchmarkTest83338(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "app_display_name";
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{secretValue});
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
