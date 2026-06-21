// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22589 {

    @PostMapping("/BenchmarkTest22589")
    public void BenchmarkTest22589(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        Integer.parseInt(commentValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
