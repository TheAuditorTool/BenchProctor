// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75864 {

    @GetMapping("/BenchmarkTest75864/{pathId}")
    public void BenchmarkTest75864(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        if (!pathValue.endsWith(".jpg") && !pathValue.endsWith(".png")) { response.sendError(400); return; }
        String entryFile = pathValue;
        Files.write(Paths.get("/var/uploads/" + entryFile), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
