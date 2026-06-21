// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60838 {

    @PostMapping("/BenchmarkTest60838")
    public void BenchmarkTest60838(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : fieldValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        new java.io.File(data).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
