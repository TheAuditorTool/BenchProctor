// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03499 {

    @GetMapping("/BenchmarkTest03499")
    public void BenchmarkTest03499(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(forwardedIp, "query");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        response.sendError(500, data);
    }
}
