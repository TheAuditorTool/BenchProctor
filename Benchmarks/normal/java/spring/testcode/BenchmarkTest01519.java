// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01519 {

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest01519")
    public void BenchmarkTest01519(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        valueRef.set(uaValue);
        String data = valueRef.get();
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
