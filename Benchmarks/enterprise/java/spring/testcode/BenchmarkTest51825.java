// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest51825 {

    @GetMapping("/BenchmarkTest51825")
    public void BenchmarkTest51825(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        if (!envValue.endsWith(".jpg") && !envValue.endsWith(".png")) { response.sendError(400); return; }
        String entryFile = envValue;
        Files.write(Paths.get("/var/uploads/" + entryFile), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
