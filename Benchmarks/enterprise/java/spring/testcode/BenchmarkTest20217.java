// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest20217 {

    @GetMapping("/BenchmarkTest20217")
    public void BenchmarkTest20217(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data;
        if (cookieValue.length() > 256) { data = cookieValue.substring(0, 256); }
        else { data = cookieValue; }
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException e) {
            response.sendError(400, e.getMessage()); return;
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
