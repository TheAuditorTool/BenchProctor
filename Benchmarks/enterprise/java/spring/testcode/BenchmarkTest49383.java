// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest49383 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest49383", consumes="application/xml")
    public void BenchmarkTest49383(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = normalize(xmlValue);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(data).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String checkedPath = resolved.toString();
        String content = Files.readString(Paths.get(checkedPath), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
