// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08714 {

    @GetMapping("/BenchmarkTest08714")
    public void BenchmarkTest08714(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        response.addCookie(new Cookie("session", cookieValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
