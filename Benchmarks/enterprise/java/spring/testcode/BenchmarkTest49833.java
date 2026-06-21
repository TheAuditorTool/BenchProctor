// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest49833 {

    @GetMapping("/BenchmarkTest49833")
    public void BenchmarkTest49833(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Function<String, String> primary = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> stripChain = primary.andThen(String::trim);
        String data = stripChain.apply(userId);
        int result = 100 / Integer.parseInt(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
