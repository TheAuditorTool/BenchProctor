// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81580 {

    @GetMapping("/BenchmarkTest81580")
    public void BenchmarkTest81580(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String prefix = authHeader.length() > 0 ? authHeader.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = authHeader.toLowerCase(); break;
            case "f": data = authHeader.toUpperCase(); break;
            default: data = authHeader.strip(); break;
        }
        java.net.URL parsed = java.net.URI.create(data).toURL();
        java.util.Set<String> hosts = java.util.Set.of("api.svc.local", "cdn.acmecdn.net");
        if (!hosts.contains(parsed.getHost())) { response.sendError(403); return; }
        String targetUrl = parsed.getProtocol() + "://" + parsed.getHost() + (parsed.getPort() == -1 ? "" : ":" + parsed.getPort());
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(targetUrl)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
