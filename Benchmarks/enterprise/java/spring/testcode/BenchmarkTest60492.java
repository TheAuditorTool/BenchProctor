// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60492 {

    @GetMapping("/BenchmarkTest60492")
    public void BenchmarkTest60492(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(userId, "header");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        response.getWriter().print("<div>" + data + "</div>");
    }
}
