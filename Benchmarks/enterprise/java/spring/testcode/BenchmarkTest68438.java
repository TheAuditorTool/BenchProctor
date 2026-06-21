// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest68438 {

    @GetMapping("/BenchmarkTest68438")
    public void BenchmarkTest68438(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = String.join(" ", uaValue.split("\\s+"));
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        java.net.URL u = new java.net.URL("https://api.svc.local/lookup?q=" + data);
        java.net.HttpURLConnection hc = (java.net.HttpURLConnection) u.openConnection();
        hc.connect();
        hc.getInputStream().close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
