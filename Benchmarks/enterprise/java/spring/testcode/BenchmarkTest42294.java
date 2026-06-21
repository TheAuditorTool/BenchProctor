// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest42294 {

    @GetMapping("/BenchmarkTest42294")
    public void BenchmarkTest42294(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.function.Function<String, String> initialFn = s -> s.replace("\r", "").replace("\n", "");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::strip);
        String data = transformed.apply(refererValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", processed)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
