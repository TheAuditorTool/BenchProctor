// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest37555 {

    @GetMapping("/BenchmarkTest37555")
    public void BenchmarkTest37555(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(uaValue, "query");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
    }
}
