// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04562 {

    @GetMapping("/BenchmarkTest04562")
    public void BenchmarkTest04562(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(headerValue);
        String data = bundle.toString();
        String normalizedPath = java.nio.file.Paths.get(data).normalize().toString();
        Files.write(Paths.get("/var/uploads/" + normalizedPath), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
