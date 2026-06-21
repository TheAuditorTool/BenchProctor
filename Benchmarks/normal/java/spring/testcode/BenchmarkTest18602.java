// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18602 {

    @PostMapping("/BenchmarkTest18602")
    public void BenchmarkTest18602(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.function.Function<String, String> firstStage = s -> s.replace("\r", "").replace("\n", "");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::strip);
        String data = composed.apply(commentValue);
        if (!data.matches("^[\\w\\s.\\-:/=\\r\\n]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        response.getWriter().print(String.valueOf(data));
    }
}
