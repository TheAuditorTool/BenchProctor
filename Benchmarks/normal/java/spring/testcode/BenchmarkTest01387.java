// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01387 {

    @GetMapping("/BenchmarkTest01387")
    public void BenchmarkTest01387(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        response.setHeader("Access-Control-Allow-Origin", forwardedIp);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
