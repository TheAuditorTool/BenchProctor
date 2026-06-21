// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest67089 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest67089")
    public void BenchmarkTest67089(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data = normalize(headerValue);
        java.net.URI parsedUri = java.net.URI.create(data.contains("://") ? data : "https://" + data);
        java.net.InetAddress addr = java.net.InetAddress.getByName(parsedUri.getHost());
        if (addr.isAnyLocalAddress() || addr.isLoopbackAddress() || addr.isSiteLocalAddress() || addr.isLinkLocalAddress()) {
            response.sendError(403); return;
        }
        String targetUrl = parsedUri.getScheme() + "://" + parsedUri.getHost() + (parsedUri.getPort() == -1 ? "" : ":" + parsedUri.getPort());
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(targetUrl)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
