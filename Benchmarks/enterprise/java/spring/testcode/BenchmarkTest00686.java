// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00686 {

    @GetMapping("/BenchmarkTest00686")
    public void BenchmarkTest00686(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String argValue = java.util.Optional.ofNullable(System.getProperty("argv.value", "")).orElse("");
        StringBuilder payload = new StringBuilder();
        payload.append(argValue);
        String data = payload.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        Files.delete(Paths.get("/var/app/data/" + processed));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
