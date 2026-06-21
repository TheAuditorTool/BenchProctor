// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest67219 {

    @PostMapping(path="/BenchmarkTest67219", consumes="text/plain")
    public void BenchmarkTest67219(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", rawData);
        String data = sw.toString();
        java.net.URL parsed = java.net.URI.create(data).toURL();
        java.util.Set<String> hosts = java.util.Set.of("api.svc.local", "cdn.acmecdn.net");
        if (!hosts.contains(parsed.getHost())) { response.sendError(403); return; }
        String targetUrl = parsed.getProtocol() + "://" + parsed.getHost() + (parsed.getPort() == -1 ? "" : ":" + parsed.getPort());
        response.sendRedirect(targetUrl);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
