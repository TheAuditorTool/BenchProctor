// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest19301 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @PostMapping("/BenchmarkTest19301")
    public void BenchmarkTest19301(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = stripCRLF(commentValue);
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
