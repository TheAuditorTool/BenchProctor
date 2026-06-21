// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08484 {

    @GetMapping("/BenchmarkTest08484")
    public void BenchmarkTest08484(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String propValue = java.util.Optional.ofNullable(System.getProperty("app.value", "")).orElse("");
        String prefix = propValue.length() > 0 ? propValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = propValue.toLowerCase(); break;
            case "f": data = propValue.toUpperCase(); break;
            default: data = propValue.strip(); break;
        }
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
