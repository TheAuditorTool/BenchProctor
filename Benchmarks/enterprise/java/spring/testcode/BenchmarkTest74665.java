// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest74665 {

    @PostMapping("/BenchmarkTest74665")
    public void BenchmarkTest74665(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        StringBuilder carrier = new StringBuilder();
        carrier.append(commentValue);
        String data = carrier.toString();
        response.sendError(500, data);
    }
}
