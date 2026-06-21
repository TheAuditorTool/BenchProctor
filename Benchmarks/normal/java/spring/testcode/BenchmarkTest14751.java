// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14751 {

    @GetMapping("/BenchmarkTest14751")
    public void BenchmarkTest14751(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        StringBuilder payload = new StringBuilder();
        payload.append(cookieValue);
        String data = payload.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        if ("admin".equals(processed)) {
            response.getWriter().print("{\"role\":\"admin\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
