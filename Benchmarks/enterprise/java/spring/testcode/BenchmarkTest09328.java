// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09328 {

    @GetMapping("/BenchmarkTest09328")
    public void BenchmarkTest09328(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        System.loadLibrary(forwardedIp);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
