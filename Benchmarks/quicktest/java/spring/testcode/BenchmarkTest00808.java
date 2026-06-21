// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00808 {

    @PostMapping("/BenchmarkTest00808")
    public void BenchmarkTest00808(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(commentValue, "http");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        response.getWriter().print("<div>" + data + "</div>");
    }
}
