// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01924 {

    @GetMapping("/BenchmarkTest01924")
    public void BenchmarkTest01924(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String yamlValue = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/etc/app/config.yaml")))).orElse("");
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(yamlValue, "header");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
