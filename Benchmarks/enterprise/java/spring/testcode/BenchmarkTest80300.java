// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80300 {

    @GetMapping("/BenchmarkTest80300")
    public void BenchmarkTest80300(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(forwardedIp, "header");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        response.sendError(500, data);
    }
}
