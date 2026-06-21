// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest63851 {

    @GetMapping("/BenchmarkTest63851")
    public void BenchmarkTest63851(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{userId});
        try {
            Integer.parseInt(data);
        } catch (Exception e) { }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
