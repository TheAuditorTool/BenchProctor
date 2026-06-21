// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18253 {

    @GetMapping("/BenchmarkTest18253")
    public void BenchmarkTest18253(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.function.Function<String, String> primary = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> stripChain = primary.andThen(String::trim);
        String data = stripChain.apply(authHeader);
        if (!new java.io.File("/var/app/data", new java.io.File(data).getName()).delete()) { response.sendError(500, "delete failed"); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
