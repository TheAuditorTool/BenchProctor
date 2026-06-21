// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13144 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest13144")
    public void BenchmarkTest13144(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = trimEnds(hostValue);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
