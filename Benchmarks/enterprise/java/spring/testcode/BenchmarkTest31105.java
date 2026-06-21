// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest31105 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest31105")
    public void BenchmarkTest31105(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = normalize(commentValue);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
