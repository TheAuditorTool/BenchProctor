// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest50073 {

    @GetMapping("/BenchmarkTest50073/{pathId}")
    public void BenchmarkTest50073(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{pathValue});
        if (!data.isEmpty()) throw new IllegalArgumentException("invalid input: " + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
