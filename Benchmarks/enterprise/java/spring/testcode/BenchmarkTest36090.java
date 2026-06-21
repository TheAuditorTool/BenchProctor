// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36090 {

    @GetMapping("/BenchmarkTest36090/{pathId}")
    public void BenchmarkTest36090(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(pathValue, "form");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
