// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08274 {

    @PostMapping(path="/BenchmarkTest08274", consumes="text/plain")
    public void BenchmarkTest08274(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(rawData, "form");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        new ProcessBuilder("echo", data).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
