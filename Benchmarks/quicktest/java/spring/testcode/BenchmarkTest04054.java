// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04054 {

    private enum AllowedValue { PLAIN, MARKDOWN, HTML, TEXT }

    @GetMapping("/BenchmarkTest04054")
    public void BenchmarkTest04054(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(userId, "body");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        response.getWriter().print("<div>" + data + "</div>");
    }
}
