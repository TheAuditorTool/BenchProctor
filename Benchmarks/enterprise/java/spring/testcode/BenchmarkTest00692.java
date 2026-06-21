// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00692 {

    @PostMapping("/BenchmarkTest00692")
    public void BenchmarkTest00692(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(commentValue, "header");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        response.sendError(500, data);
    }
}
