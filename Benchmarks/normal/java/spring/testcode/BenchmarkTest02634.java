// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02634 {

    @GetMapping("/BenchmarkTest02634")
    public void BenchmarkTest02634(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String processed = org.owasp.encoder.Encode.forHtml(cookieValue);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
