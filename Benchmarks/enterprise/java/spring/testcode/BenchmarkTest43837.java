// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest43837 {

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest43837")
    public void BenchmarkTest43837(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        valueRef.set(headerValue);
        String data = valueRef.get();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            new Socket(data, 80).close();
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
