// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12968 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @GetMapping("/BenchmarkTest12968")
    public void BenchmarkTest12968(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = expandTabs(authHeader);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
