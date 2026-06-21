// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest07516 {

    @GetMapping("/BenchmarkTest07516")
    public void BenchmarkTest07516(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = String.format("%s", originValue);
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(data)) { response.sendError(403); return; }
        String checkedPath = "/var/app/data/" + data;
        Files.delete(Paths.get(checkedPath));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
