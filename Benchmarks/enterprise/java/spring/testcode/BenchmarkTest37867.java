// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest37867 {

    @PostMapping("/BenchmarkTest37867")
    public void BenchmarkTest37867(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        try {
            Integer.parseInt(commentValue);
        } catch (Exception e) { }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
