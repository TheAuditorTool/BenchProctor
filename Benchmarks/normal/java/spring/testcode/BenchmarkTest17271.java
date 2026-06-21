// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17271 {

    @GetMapping("/BenchmarkTest17271")
    public void BenchmarkTest17271(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        response.setHeader("Refresh", "0; url=" + cookieValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
