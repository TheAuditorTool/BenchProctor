// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest26090 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest26090")
    public void BenchmarkTest26090(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data = normalize(cookieValue);
        response.sendError(500, data);
    }
}
