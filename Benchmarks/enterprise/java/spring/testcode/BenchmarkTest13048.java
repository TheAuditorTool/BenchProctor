// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13048 {

    @GetMapping("/BenchmarkTest13048")
    public void BenchmarkTest13048(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("\\s+", " ");
        String data = transform.apply(forwardedIp);
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException e) { response.sendError(400); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
