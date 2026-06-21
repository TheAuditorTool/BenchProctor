// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60459 {

    @GetMapping("/BenchmarkTest60459")
    public void BenchmarkTest60459(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(authHeader, "query");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        response.sendError(500, data);
    }
}
