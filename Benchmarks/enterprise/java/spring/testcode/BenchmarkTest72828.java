// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest72828 {

    @GetMapping("/BenchmarkTest72828")
    public void BenchmarkTest72828(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        if (!cookieValue.isEmpty()) throw new IllegalArgumentException("invalid input: " + cookieValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
