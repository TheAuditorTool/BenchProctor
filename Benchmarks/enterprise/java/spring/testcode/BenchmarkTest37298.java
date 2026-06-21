// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest37298 {

    @PostMapping("/BenchmarkTest37298")
    public void BenchmarkTest37298(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        request.getSession().setAttribute("data", String.valueOf(commentValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
