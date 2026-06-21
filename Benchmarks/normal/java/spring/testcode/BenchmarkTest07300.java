// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest07300 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest07300")
    public void BenchmarkTest07300(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = normalize(forwardedIp);
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
