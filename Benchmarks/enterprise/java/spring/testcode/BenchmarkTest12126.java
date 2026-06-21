// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12126 {

    @GetMapping("/BenchmarkTest12126")
    public void BenchmarkTest12126(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(hostValue)) { response.sendError(403); return; }
        String allowedBin = hostValue;
        System.loadLibrary(allowedBin);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
