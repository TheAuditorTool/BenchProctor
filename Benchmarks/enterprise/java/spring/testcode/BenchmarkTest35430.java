// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest35430 {

    @GetMapping("/BenchmarkTest35430")
    public void BenchmarkTest35430(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(forwardedIp);
        String data = carrier.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(processed);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
