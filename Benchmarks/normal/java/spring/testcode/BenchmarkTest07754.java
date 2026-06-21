// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest07754 {

    @GetMapping("/BenchmarkTest07754")
    public void BenchmarkTest07754(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "config_secret_test_abc123";
        String prefix = secretValue.length() > 0 ? secretValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = secretValue.toLowerCase(); break;
            case "f": data = secretValue.toUpperCase(); break;
            default: data = secretValue.strip(); break;
        }
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
