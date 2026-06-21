// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17049 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @GetMapping("/BenchmarkTest17049")
    public void BenchmarkTest17049(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = collapseWhitespace(userId);
        if (!data.matches("^[\\w\\s.;|&$`'\\\"_/\\-]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + data}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
