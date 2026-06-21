// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03910 {

    @GetMapping("/BenchmarkTest03910")
    public void BenchmarkTest03910(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.List<String> tokens = java.util.Arrays.asList(hostValue.split(","));
        String data = String.join(",", tokens);
        response.setHeader("X-Frame-Options", "DENY");
        response.setHeader("Content-Security-Policy", "frame-ancestors 'none'");
        response.getWriter().print(String.valueOf(data));
    }
}
