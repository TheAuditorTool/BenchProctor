// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest51448 {

    @PostMapping("/BenchmarkTest51448")
    public void BenchmarkTest51448(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        new java.io.File(commentValue).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
