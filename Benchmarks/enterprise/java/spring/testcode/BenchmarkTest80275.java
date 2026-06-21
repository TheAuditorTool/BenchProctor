// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80275 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest80275")
    public void BenchmarkTest80275(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = stripWhitespace(uaValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        if ("admin".equals(processed) || "ROLE_ADMIN".equals(processed)) {
            response.getWriter().print("{\"status\":\"ok\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
