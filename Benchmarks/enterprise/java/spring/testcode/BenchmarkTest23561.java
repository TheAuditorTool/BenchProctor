// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest23561 {

    @GetMapping("/BenchmarkTest23561")
    public void BenchmarkTest23561(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        response.addCookie(new Cookie("session", headerValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
