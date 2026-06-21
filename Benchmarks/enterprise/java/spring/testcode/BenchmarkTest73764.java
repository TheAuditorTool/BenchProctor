// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73764 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest73764/{pathId}")
    public void BenchmarkTest73764(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = normalize(pathValue);
        Files.delete(Paths.get("/var/app/data/" + data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
