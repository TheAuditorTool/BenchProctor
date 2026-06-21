// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest67150 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest67150")
    public void BenchmarkTest67150(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data = trimEnds(cookieValue);
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
