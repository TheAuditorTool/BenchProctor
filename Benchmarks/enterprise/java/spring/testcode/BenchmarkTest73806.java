// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73806 {

    @GetMapping("/BenchmarkTest73806")
    public void BenchmarkTest73806(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        response.addCookie(new Cookie("session", forwardedIp));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
