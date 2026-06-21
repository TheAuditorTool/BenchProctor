// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest65936 {

    @PostMapping("/BenchmarkTest65936")
    public void BenchmarkTest65936(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        StringBuilder payload = new StringBuilder();
        payload.append(commentValue);
        String data = payload.toString();
        String processed = data.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;");
        response.setHeader("Refresh", "0; url=" + processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
