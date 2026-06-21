// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest53702 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @PostMapping("/BenchmarkTest53702")
    public void BenchmarkTest53702(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = expandTabs(commentValue);
        response.getWriter().print(String.valueOf(data));
    }
}
