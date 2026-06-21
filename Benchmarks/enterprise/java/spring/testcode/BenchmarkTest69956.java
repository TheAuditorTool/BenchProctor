// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest69956 {

    @PostMapping("/BenchmarkTest69956")
    public void BenchmarkTest69956(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(commentValue, "header");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        response.getWriter().print(String.valueOf(data));
    }
}
