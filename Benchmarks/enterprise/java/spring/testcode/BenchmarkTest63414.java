// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest63414 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest63414")
    public void BenchmarkTest63414(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = normalize(commentValue);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
