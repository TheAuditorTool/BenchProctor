// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest68604 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @PostMapping(path="/BenchmarkTest68604", consumes="application/xml")
    public void BenchmarkTest68604(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = toLowerCase(xmlValue);
        if (System.currentTimeMillis() > 1000000000000L) {
            String content = Files.readString(Paths.get("/var/app/data/" + data), java.nio.charset.StandardCharsets.UTF_8);
            response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
