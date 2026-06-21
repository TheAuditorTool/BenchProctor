// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04659 {

    @GetMapping("/BenchmarkTest04659")
    public void BenchmarkTest04659(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Function<String, String> initialFn = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::strip);
        String data = transformed.apply(userId);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        byte[] buf = new byte[Integer.parseInt(processed)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
