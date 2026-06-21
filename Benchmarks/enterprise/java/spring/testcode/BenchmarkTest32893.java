// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest32893 {

    @GetMapping("/BenchmarkTest32893")
    public void BenchmarkTest32893(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        if (!("true".equals(cookieValue) || "false".equals(cookieValue))) { response.sendError(400); return; }
        java.util.regex.Pattern inputPattern = java.util.regex.Pattern.compile("[a-zA-Z0-9_-]+");
        if (inputPattern.matcher(cookieValue).find()) {
            response.setHeader("X-Validated-Input", cookieValue);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
