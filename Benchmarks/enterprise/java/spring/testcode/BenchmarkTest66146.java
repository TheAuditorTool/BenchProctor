// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest66146 {

    @PostMapping("/BenchmarkTest66146")
    public void BenchmarkTest66146(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(fieldValue, "form");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        response.setContentType("application/json");
        response.getWriter().print("{\"echo\":\"" + data + "\"}");
    }
}
