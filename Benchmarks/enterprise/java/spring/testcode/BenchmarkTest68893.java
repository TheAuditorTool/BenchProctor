// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest68893 {

    @PostMapping("/BenchmarkTest68893")
    public void BenchmarkTest68893(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        StringBuilder envelope = new StringBuilder();
        envelope.append(commentValue);
        String data = envelope.toString();
        int boundedVal;
        try { boundedVal = Integer.parseInt(data); }
        catch (NumberFormatException e) { response.sendError(400); return; }
        if (boundedVal < 0 || boundedVal > 1048576) { response.sendError(400); return; }
        long requested = boundedVal;
        long allocSize = requested + 1;
        response.setHeader("X-Alloc-Size", String.valueOf(allocSize));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
