// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73224 {

    @GetMapping("/BenchmarkTest73224")
    public void BenchmarkTest73224(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(userId);
        String data = wrapper.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        java.util.HashMap<String,Object> entity = new java.util.HashMap<>();
        String[] formPair = processed.split("=", 2);
        if (formPair.length == 2) {
            entity.put(formPair[0], formPair[1]);
            response.setHeader("X-Field-Set", formPair[0]);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
