// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest70198 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest70198")
    public void BenchmarkTest70198(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data = trimEnds(cookieValue);
        response.sendError(500, data);
    }
}
