// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest79447 {

    @PostMapping(path="/BenchmarkTest79447", consumes="text/plain")
    public void BenchmarkTest79447(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(rawData, "request");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        request.isUserInRole("ADMIN");
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
