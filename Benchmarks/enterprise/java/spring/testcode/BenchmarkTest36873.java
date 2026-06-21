// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36873 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @GetMapping("/BenchmarkTest36873")
    public void BenchmarkTest36873(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = collapseWhitespace(uaValue);
        String processed = data.replace("\r", "").replace("\n", "").replaceAll("[A-Za-z0-9]{4,}", "****");
        response.setHeader("X-Forwarded-For", processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
