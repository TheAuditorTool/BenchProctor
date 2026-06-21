// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18580 {

    @PostMapping("/BenchmarkTest18580")
    public void BenchmarkTest18580(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(commentValue, "header");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        response.sendError(500, data);
    }
}
