// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15469 {

    @GetMapping("/BenchmarkTest15469")
    public void BenchmarkTest15469(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        response.addCookie(new Cookie("session", forwardedIp));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
