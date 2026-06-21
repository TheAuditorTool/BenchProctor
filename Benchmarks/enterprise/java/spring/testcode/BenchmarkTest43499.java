// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest43499 {

    @PostMapping(path="/BenchmarkTest43499", consumes="text/plain")
    public void BenchmarkTest43499(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(rawData, "query");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        response.getWriter().print("<div>" + data + "</div>");
    }
}
