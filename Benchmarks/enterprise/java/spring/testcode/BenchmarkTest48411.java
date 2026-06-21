// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest48411 {

    @PostMapping(path="/BenchmarkTest48411", consumes="text/plain")
    public void BenchmarkTest48411(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(rawData, "query");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        System.loadLibrary(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
