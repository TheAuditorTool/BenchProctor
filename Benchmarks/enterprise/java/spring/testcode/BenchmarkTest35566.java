// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest35566 {

    private static String trimEnds(String v) { return v.trim(); }

    @PostMapping(path="/BenchmarkTest35566", consumes="text/plain")
    public void BenchmarkTest35566(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = trimEnds(rawData);
        if ("admin".equals(data)) {
            response.getWriter().print("{\"role\":\"admin\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
