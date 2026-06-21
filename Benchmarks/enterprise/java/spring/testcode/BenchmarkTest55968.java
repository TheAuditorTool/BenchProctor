// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest55968 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @PostMapping(path="/BenchmarkTest55968", consumes="text/plain")
    public void BenchmarkTest55968(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = toLowerCase(rawData);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        java.util.regex.Pattern inputPattern = java.util.regex.Pattern.compile("[a-zA-Z0-9_-]+");
        if (inputPattern.matcher(processed).find()) {
            response.setHeader("X-Validated-Input", processed);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
