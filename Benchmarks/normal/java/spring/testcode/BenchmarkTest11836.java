// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest11836 {

    @GetMapping("/BenchmarkTest11836")
    public void BenchmarkTest11836(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String argValue = java.util.Optional.ofNullable(System.getProperty("argv.value", "")).orElse("");
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", argValue);
        String data = sw.toString();
        String checkedPath = "/var/app/data/" + java.nio.file.Paths.get(data).getFileName().toString();
        Files.delete(Paths.get(checkedPath));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
