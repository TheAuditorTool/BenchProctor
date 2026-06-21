// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22529 {

    @GetMapping("/BenchmarkTest22529")
    public void BenchmarkTest22529(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(userId, "json");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        response.getWriter().print("<div>" + data + "</div>");
    }
}
