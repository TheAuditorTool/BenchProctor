// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest49794 {

    @PostMapping("/BenchmarkTest49794")
    public void BenchmarkTest49794(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("\\s+", " ");
        String data = transform.apply(commentValue);
        new java.io.File(data).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
