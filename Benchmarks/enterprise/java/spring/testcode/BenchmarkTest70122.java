// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest70122 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @PostMapping(path="/BenchmarkTest70122", consumes="text/plain")
    public void BenchmarkTest70122(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = toLowerCase(rawData);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            String content = Files.readString(Paths.get("/var/app/data/" + data), java.nio.charset.StandardCharsets.UTF_8);
            response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
