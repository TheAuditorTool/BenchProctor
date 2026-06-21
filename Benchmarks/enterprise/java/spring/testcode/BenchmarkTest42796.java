// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest42796 {

    private static final java.util.concurrent.atomic.AtomicReference<String> atomicValue = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest42796")
    public void BenchmarkTest42796(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        atomicValue.set(headerValue);
        String data = atomicValue.get();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
        }
    }
}
