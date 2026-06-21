// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest57274 {

    @GetMapping("/BenchmarkTest57274")
    public void BenchmarkTest57274(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = String.format("payload=%s", hostValue);
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(data)) { response.sendError(403); return; }
        String allowedBin = data;
        System.loadLibrary(allowedBin);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
