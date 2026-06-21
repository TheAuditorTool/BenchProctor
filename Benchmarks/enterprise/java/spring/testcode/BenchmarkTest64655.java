// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.util.Random;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64655 {

    @PostMapping(path="/BenchmarkTest64655", consumes="application/xml")
    public void BenchmarkTest64655(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        byte[] tokenBytes = new byte[32];
        new java.security.SecureRandom().nextBytes(tokenBytes);
        String randToken = java.util.HexFormat.of().formatHex(tokenBytes);
        response.setHeader("X-Rand", randToken);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
