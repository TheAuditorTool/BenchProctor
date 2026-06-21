// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest72944 {

    @GetMapping("/BenchmarkTest72944")
    public void BenchmarkTest72944(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data;
        if (forwardedIp.length() > 256) { data = forwardedIp.substring(0, 256); }
        else { data = forwardedIp; }
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + data});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
