// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest67929 {

    @GetMapping("/BenchmarkTest67929")
    public void BenchmarkTest67929(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        if ("https://app.acmecdn.net".equals(cookieValue)) response.setHeader("Access-Control-Allow-Origin", cookieValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
