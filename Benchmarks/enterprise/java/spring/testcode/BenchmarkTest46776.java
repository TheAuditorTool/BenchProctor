// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest46776 {

    @PostMapping("/BenchmarkTest46776")
    public void BenchmarkTest46776(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data;
        try { data = String.valueOf(Integer.parseInt(commentValue)); }
        catch (NumberFormatException e) { data = commentValue; }
        new Socket(data, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
