// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00461 {

    @GetMapping("/BenchmarkTest00461")
    public void BenchmarkTest00461(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        StringBuilder payload = new StringBuilder();
        payload.append(cookieValue);
        String data = payload.toString();
        Cookie cookie = new Cookie("session", data);
        cookie.setSecure(true);
        cookie.setHttpOnly(true);
        cookie.setAttribute("SameSite", "Strict");
        cookie.setMaxAge(28800);
        response.addCookie(cookie);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
