// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02009 {

    @GetMapping("/BenchmarkTest02009/{pathId}")
    public void BenchmarkTest02009(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        if (!("true".equals(pathValue) || "false".equals(pathValue))) { response.sendError(400); return; }
        java.util.HashMap<String,Object> entity = new java.util.HashMap<>();
        String[] formPair = pathValue.split("=", 2);
        if (formPair.length == 2) {
            entity.put(formPair[0], formPair[1]);
            response.setHeader("X-Field-Set", formPair[0]);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
