// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01498 {

    @GetMapping("/BenchmarkTest01498")
    public void BenchmarkTest01498(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        String prefix = dotenvValue.length() > 0 ? dotenvValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = dotenvValue.toLowerCase(); break;
            case "f": data = dotenvValue.toUpperCase(); break;
            default: data = dotenvValue.strip(); break;
        }
        Cookie cookie = new Cookie("session", data);
        cookie.setMaxAge(86400);
        response.addCookie(cookie);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
