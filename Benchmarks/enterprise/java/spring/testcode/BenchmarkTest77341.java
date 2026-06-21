// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest77341 {

    @PostMapping("/BenchmarkTest77341")
    public void BenchmarkTest77341(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        StringBuilder payload = new StringBuilder();
        payload.append(commentValue);
        String data = payload.toString();
        if (System.currentTimeMillis() > 1000000000000L) {
            response.getWriter().print("<div>" + data + "</div>");
        }
    }
}
