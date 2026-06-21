// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01470 {

    @GetMapping("/BenchmarkTest01470")
    public void BenchmarkTest01470(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(userId);
        String data = normalizer.apply(userId);
        java.net.URI parsedUri = java.net.URI.create(data.contains("://") ? data : "https://" + data);
        java.net.InetAddress addr = java.net.InetAddress.getByName(parsedUri.getHost());
        if (addr.isAnyLocalAddress() || addr.isLoopbackAddress() || addr.isSiteLocalAddress() || addr.isLinkLocalAddress()) {
            response.sendError(403); return;
        }
        String targetUrl = parsedUri.getScheme() + "://" + parsedUri.getHost() + (parsedUri.getPort() == -1 ? "" : ":" + parsedUri.getPort());
        new Socket(targetUrl, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
