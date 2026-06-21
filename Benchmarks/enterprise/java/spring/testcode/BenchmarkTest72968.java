// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest72968 {

    private static final java.util.concurrent.atomic.AtomicReference<String> stateBox = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest72968")
    public void BenchmarkTest72968(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        stateBox.set(uaValue);
        String data = stateBox.get();
        if (System.currentTimeMillis() > 1000000000000L) {
            response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
        }
    }
}
