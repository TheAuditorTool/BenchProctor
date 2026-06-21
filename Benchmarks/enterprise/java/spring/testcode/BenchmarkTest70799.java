// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest70799 {

    @PostMapping(path="/BenchmarkTest70799", consumes="application/xml")
    public void BenchmarkTest70799(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = String.format("payload=%s", xmlValue);
        String checkedPath = "/var/app/data/" + java.nio.file.Paths.get(data).getFileName().toString();
        Files.delete(Paths.get(checkedPath));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
