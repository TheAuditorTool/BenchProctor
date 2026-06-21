// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02952 {

    private static final java.util.concurrent.atomic.AtomicReference<String> ref = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest02952")
    public void BenchmarkTest02952(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        ref.set(refererValue);
        String data = ref.get();
        String processed = data.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;");
        response.setHeader("Refresh", "0; url=" + processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
