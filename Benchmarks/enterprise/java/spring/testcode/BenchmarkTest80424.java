// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80424 {

    @GetMapping("/BenchmarkTest80424")
    public void BenchmarkTest80424(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String processed = org.owasp.encoder.Encode.forHtml(cookieValue);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
