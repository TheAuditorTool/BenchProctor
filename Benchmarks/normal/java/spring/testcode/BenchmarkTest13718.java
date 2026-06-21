// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13718 {

    @PostMapping("/BenchmarkTest13718")
    public void BenchmarkTest13718(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(commentValue, "body");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
    }
}
