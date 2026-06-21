// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18434 {

    @PostMapping("/BenchmarkTest18434")
    public void BenchmarkTest18434(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(fieldValue, "form");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        response.setContentType("application/json");
        response.getWriter().print("{\"echo\":\"" + data + "\"}");
    }
}
