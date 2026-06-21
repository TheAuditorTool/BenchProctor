// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest71823 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @GetMapping("/BenchmarkTest71823")
    public void BenchmarkTest71823(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = collapseWhitespace(originValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        String content = Files.readString(Paths.get("/var/app/data/" + processed), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
