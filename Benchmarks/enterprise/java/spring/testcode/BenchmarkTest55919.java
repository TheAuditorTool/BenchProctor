// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest55919 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest55919")
    public void BenchmarkTest55919(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = normalize(forwardedIp);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
