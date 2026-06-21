// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest19961 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest19961")
    public void BenchmarkTest19961(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = normalize(fieldValue);
        Files.delete(Paths.get("/var/app/data/" + data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
