// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest65855 {

    @GetMapping("/BenchmarkTest65855")
    public void BenchmarkTest65855(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data;
        if (userId.length() > 256) { data = userId.substring(0, 256); }
        else { data = userId; }
        String processed = org.owasp.encoder.Encode.forHtml(data);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
