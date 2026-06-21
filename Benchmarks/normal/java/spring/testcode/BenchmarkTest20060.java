// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest20060 {

    @GetMapping("/BenchmarkTest20060")
    public void BenchmarkTest20060(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        if (!originValue.endsWith(".jpg") && !originValue.endsWith(".png")) { response.sendError(400); return; }
        String entryFile = originValue;
        Files.write(Paths.get("/var/uploads/" + entryFile), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
