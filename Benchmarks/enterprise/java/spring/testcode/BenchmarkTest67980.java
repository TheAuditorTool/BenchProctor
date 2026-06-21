// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest67980 {

    @GetMapping("/BenchmarkTest67980")
    public void BenchmarkTest67980(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(cookieValue);
        String data = carrier.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.addCookie(new Cookie("session", processed));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
