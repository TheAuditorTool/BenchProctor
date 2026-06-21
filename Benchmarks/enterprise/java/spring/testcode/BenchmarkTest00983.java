// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00983 {

    @GetMapping("/BenchmarkTest00983")
    public void BenchmarkTest00983(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(cookieValue)); }
        catch (NumberFormatException e) { data = cookieValue; }
        response.addCookie(new Cookie("session", data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
