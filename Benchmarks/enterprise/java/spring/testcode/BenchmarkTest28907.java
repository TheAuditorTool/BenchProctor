// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest28907 {

    @GetMapping("/BenchmarkTest28907")
    public void BenchmarkTest28907(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        response.addCookie(new Cookie("session", userId));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
