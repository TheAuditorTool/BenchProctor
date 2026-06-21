// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22135 {

    @GetMapping("/BenchmarkTest22135")
    public void BenchmarkTest22135(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        response.addCookie(new Cookie("session", userId));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
