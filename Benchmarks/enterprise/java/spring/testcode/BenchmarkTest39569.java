// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest39569 {

    @GetMapping("/BenchmarkTest39569")
    public void BenchmarkTest39569(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(authHeader, "json");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        response.sendError(500, data);
    }
}
