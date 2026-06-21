// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest77167 {

    @GetMapping("/BenchmarkTest77167")
    public void BenchmarkTest77167(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("\\s+", " ");
        String data = transform.apply(dotenvValue);
        String oldSessionId = request.getSession().getId();
        request.getSession().invalidate();
        request.getSession(true).setAttribute("rotated_from", oldSessionId);
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
