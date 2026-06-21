// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest11971 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest11971")
    public void BenchmarkTest11971(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = normalize(fieldValue);
        String checkedPath = "/var/app/data/" + java.nio.file.Paths.get(data).getFileName().toString();
        Files.delete(Paths.get(checkedPath));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
