// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest47459 {

    @PostMapping("/BenchmarkTest47459")
    public void BenchmarkTest47459(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        System.loadLibrary(commentValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
