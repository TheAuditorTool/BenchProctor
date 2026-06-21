// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest45089 {

    @PostMapping("/BenchmarkTest45089")
    public void BenchmarkTest45089(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        response.addCookie(new Cookie("session", commentValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
