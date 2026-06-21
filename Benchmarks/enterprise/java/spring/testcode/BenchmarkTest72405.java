// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest72405 {

    @PostMapping("/BenchmarkTest72405")
    public void BenchmarkTest72405(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(fieldValue, "cookie");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        response.getWriter().print("<div>" + data + "</div>");
    }
}
