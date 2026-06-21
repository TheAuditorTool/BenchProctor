// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest41499 {

    @GetMapping("/BenchmarkTest41499")
    public void BenchmarkTest41499(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        java.util.List<String> tokens = java.util.Arrays.asList(forwardedIp.split(","));
        String data = String.join(",", tokens);
        java.nio.file.Path resolvedBase = java.nio.file.Paths.get("/var/app/data").toAbsolutePath();
        java.nio.file.Path requested = resolvedBase.resolve(data).normalize();
        if (!requested.startsWith(resolvedBase)) { response.sendError(403, "outside safe scope"); return; }
        Runtime.getRuntime().exec(new String[]{"chown", "appuser:appgroup", requested.toString()}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
    }
}
