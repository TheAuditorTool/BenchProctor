// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14620 {

    private static String trimEnds(String v) { return v.trim(); }

    @PostMapping(path="/BenchmarkTest14620", consumes="text/plain")
    public void BenchmarkTest14620(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = trimEnds(rawData);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.setHeader("Access-Control-Allow-Origin", processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
