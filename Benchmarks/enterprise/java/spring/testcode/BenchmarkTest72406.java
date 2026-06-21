// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest72406 {

    private static final java.util.concurrent.atomic.AtomicReference<String> atomicValue = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest72406")
    public void BenchmarkTest72406(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        atomicValue.set(uaValue);
        String data = atomicValue.get();
        try {
            Integer.parseInt(data);
        } catch (Exception ignored) {
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
