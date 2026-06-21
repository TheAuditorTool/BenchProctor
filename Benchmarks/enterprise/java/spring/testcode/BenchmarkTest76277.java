// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest76277 {

    @GetMapping("/BenchmarkTest76277")
    public void BenchmarkTest76277(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(forwardedIp, "cookie");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        response.sendError(500, data);
    }
}
