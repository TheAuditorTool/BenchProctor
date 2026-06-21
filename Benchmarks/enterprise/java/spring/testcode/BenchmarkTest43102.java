// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest43102 {

    @PostMapping("/BenchmarkTest43102")
    public void BenchmarkTest43102(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(fieldValue, "body");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
    }
}
