// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22087 {

    @GetMapping("/BenchmarkTest22087")
    public void BenchmarkTest22087(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = String.format("%s", userId);
        if (!data.endsWith(".jpg") && !data.endsWith(".png")) { response.sendError(400); return; }
        String entryFile = data;
        Files.write(Paths.get("/var/uploads/" + entryFile), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
