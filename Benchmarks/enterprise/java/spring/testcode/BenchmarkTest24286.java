// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest24286 {

    @GetMapping("/BenchmarkTest24286/{pathId}")
    public void BenchmarkTest24286(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        if (!pathValue.isEmpty()) throw new IllegalArgumentException("invalid input: " + pathValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
