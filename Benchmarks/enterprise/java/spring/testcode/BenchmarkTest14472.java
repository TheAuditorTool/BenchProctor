// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14472 {

    @PostMapping("/BenchmarkTest14472")
    public void BenchmarkTest14472(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.function.Function<String, String> firstStage = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::strip);
        String data = composed.apply(fieldValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.getWriter().print("{\"resource\":\"" + processed + "\"}");
    }
}
