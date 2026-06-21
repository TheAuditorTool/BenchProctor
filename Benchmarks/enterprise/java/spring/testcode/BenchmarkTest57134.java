// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.util.Random;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest57134 {

    @GetMapping("/BenchmarkTest57134")
    public void BenchmarkTest57134(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        byte[] tokenBytes = new byte[32];
        new java.security.SecureRandom().nextBytes(tokenBytes);
        String randToken = java.util.HexFormat.of().formatHex(tokenBytes);
        response.setHeader("X-Rand", randToken);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
