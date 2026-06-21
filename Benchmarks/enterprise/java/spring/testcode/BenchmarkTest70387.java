// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest70387 {

    @GetMapping("/BenchmarkTest70387")
    public void BenchmarkTest70387(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(cookieValue, "query");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        response.sendError(500, data);
    }
}
