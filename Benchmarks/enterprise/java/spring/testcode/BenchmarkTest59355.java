// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest59355 {

    @PostMapping("/BenchmarkTest59355")
    public void BenchmarkTest59355(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        if ("https://app.acmecdn.net".equals(commentValue)) response.setHeader("Access-Control-Allow-Origin", commentValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
