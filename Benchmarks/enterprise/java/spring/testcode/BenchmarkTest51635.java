// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest51635 {

    @GetMapping("/BenchmarkTest51635")
    public void BenchmarkTest51635(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        response.addCookie(new Cookie("session", refererValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
