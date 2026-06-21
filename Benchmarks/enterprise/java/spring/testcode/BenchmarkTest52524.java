// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest52524 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @PostMapping("/BenchmarkTest52524")
    public void BenchmarkTest52524(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = toLowerCase(fieldValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        Cookie cookie = new Cookie("session", processed);
        cookie.setMaxAge(86400);
        response.addCookie(cookie);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
