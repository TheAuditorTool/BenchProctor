// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest49120 {

    @GetMapping("/BenchmarkTest49120")
    public void BenchmarkTest49120(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String prefix = forwardedIp.length() > 0 ? forwardedIp.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = forwardedIp.toLowerCase(); break;
            case "f": data = forwardedIp.toUpperCase(); break;
            default: data = forwardedIp.strip(); break;
        }
        Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
