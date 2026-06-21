// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10768 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest10768")
    public void BenchmarkTest10768(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadedName = java.util.Optional.ofNullable((String) request.getAttribute("uploadName")).orElse("");
        String data = trimEnds(uploadedName);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
