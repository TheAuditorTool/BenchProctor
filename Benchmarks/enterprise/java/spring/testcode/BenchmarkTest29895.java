// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest29895 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest29895")
    public void BenchmarkTest29895(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = normalize(commentValue);
        response.getWriter().print(String.valueOf(data));
    }
}
