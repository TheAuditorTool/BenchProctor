// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest41985 {

    @GetMapping("/BenchmarkTest41985")
    public void BenchmarkTest41985(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(originValue, "json");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
    }
}
