// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64780 {

    private static final java.util.concurrent.atomic.AtomicReference<String> atomicValue = new java.util.concurrent.atomic.AtomicReference<>();
    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest64780.class);

    @GetMapping("/BenchmarkTest64780")
    public void BenchmarkTest64780(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        atomicValue.set(forwardedIp);
        String data = atomicValue.get();
        LOG.info("request processed");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
