// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest76571 {

    @GetMapping("/BenchmarkTest76571")
    public void BenchmarkTest76571(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(userId, "query");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        System.loadLibrary(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
