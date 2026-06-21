// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest67103 {

    @GetMapping("/BenchmarkTest67103")
    public void BenchmarkTest67103(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        Files.delete(Paths.get("/var/app/data/" + forwardedIp));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
