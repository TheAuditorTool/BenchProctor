// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05266 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest05266")
    public void BenchmarkTest05266(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = normalize(fieldValue);
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
