// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest61930 {

    @GetMapping("/BenchmarkTest61930/{pathId}")
    public void BenchmarkTest61930(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + pathValue;
        String data = valueSupplier.get();
        response.sendRedirect(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
