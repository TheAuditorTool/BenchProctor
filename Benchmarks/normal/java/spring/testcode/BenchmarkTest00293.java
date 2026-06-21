// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00293 {

    @PostMapping("/BenchmarkTest00293")
    public void BenchmarkTest00293(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        response.setHeader("Refresh", "0; url=" + commentValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
