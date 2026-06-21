// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17801 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GetMapping("/BenchmarkTest17801")
    public void BenchmarkTest17801(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = stripCRLF(uaValue);
        java.net.URI parsed = java.net.URI.create(data);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.endsWith(".svc.local") && !parsedHost.endsWith(".acmecdn.net")) {
            response.sendError(403, "forbidden host"); return;
        }
        String targetUrl = data;
        response.setHeader("Access-Control-Allow-Origin", targetUrl);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
