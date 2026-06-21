// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15714 {

    @GetMapping("/BenchmarkTest15714")
    public void BenchmarkTest15714(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        if (!("true".equals(uaValue) || "false".equals(uaValue))) { response.sendError(400); return; }
        java.util.HashMap<String,Object> entity = new java.util.HashMap<>();
        String[] formPair = uaValue.split("=", 2);
        if (formPair.length == 2) {
            entity.put(formPair[0], formPair[1]);
            response.setHeader("X-Field-Set", formPair[0]);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
