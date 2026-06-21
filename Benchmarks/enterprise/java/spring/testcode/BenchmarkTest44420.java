// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest44420 {

    @GetMapping("/BenchmarkTest44420")
    public void BenchmarkTest44420(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        request.getSession().setAttribute("data", String.valueOf(forwardedIp));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
