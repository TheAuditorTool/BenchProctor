// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest41268 {

    @PostMapping("/BenchmarkTest41268")
    public void BenchmarkTest41268(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = commentValue.replace("\u0000", "");
        Integer.parseInt(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
