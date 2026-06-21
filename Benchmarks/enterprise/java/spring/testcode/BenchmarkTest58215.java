// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest58215 {

    @GetMapping("/BenchmarkTest58215")
    public void BenchmarkTest58215(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        Integer.parseInt(forwardedIp);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
