// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest76832 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest76832")
    public void BenchmarkTest76832(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data = normalize(cookieValue);
        response.getWriter().print(String.valueOf(data));
    }
}
