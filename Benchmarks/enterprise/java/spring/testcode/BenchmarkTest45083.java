// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest45083 {

    @GetMapping("/BenchmarkTest45083")
    public void BenchmarkTest45083(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(forwardedIp);
        String data = normalizer.apply(forwardedIp);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        request.getSession().setAttribute("data", String.valueOf(processed));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
