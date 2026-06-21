// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest26284 {

    private static final java.util.concurrent.atomic.AtomicReference<String> atomicValue = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest26284")
    public void BenchmarkTest26284(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        atomicValue.set(hostValue);
        String data = atomicValue.get();
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        String trustedClaim = data;
        response.setHeader("X-Claim-Trusted", trustedClaim);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
