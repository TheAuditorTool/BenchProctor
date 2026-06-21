// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest62341 {

    @PostMapping(path="/BenchmarkTest62341", consumes="application/xml")
    public void BenchmarkTest62341(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        StringBuilder payload = new StringBuilder();
        payload.append(xmlValue);
        String data = payload.toString();
        if (!data.endsWith(".jpg") && !data.endsWith(".png")) { response.sendError(400); return; }
        String entryFile = data;
        Files.write(Paths.get("/var/uploads/" + entryFile), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
