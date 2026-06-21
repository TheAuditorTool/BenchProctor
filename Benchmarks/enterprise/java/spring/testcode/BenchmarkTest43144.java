// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest43144 {

    @GetMapping("/BenchmarkTest43144")
    public void BenchmarkTest43144(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(userId, "http");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        response.sendError(500, data);
    }
}
