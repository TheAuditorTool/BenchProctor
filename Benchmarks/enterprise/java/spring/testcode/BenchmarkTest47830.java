// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest47830 {

    @GetMapping("/BenchmarkTest47830")
    public void BenchmarkTest47830(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = String.format("payload=%s", forwardedIp);
        response.addCookie(new Cookie("session", data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
