// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest76067 {

    @GetMapping("/BenchmarkTest76067")
    public void BenchmarkTest76067(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        response.addCookie(new Cookie("session", refererValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
