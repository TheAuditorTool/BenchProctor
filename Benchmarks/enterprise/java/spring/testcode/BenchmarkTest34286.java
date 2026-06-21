// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest34286 {

    @PostMapping(path="/BenchmarkTest34286", consumes="text/plain")
    public void BenchmarkTest34286(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.regex.Pattern inputPattern = java.util.regex.Pattern.compile("[a-zA-Z0-9_-]+");
        if (inputPattern.matcher(rawData).find()) {
            response.setHeader("X-Validated-Input", rawData);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
