// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest82598 {

    @GetMapping("/BenchmarkTest82598")
    public void BenchmarkTest82598(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(uaValue);
        String data = envelope.toString();
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
    }
}
