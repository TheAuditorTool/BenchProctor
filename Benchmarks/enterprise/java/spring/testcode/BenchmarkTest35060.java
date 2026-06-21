// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest35060 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @GetMapping("/BenchmarkTest35060")
    public void BenchmarkTest35060(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = expandTabs(uaValue);
        java.util.HashMap<String,Object> entity = new java.util.HashMap<>();
        String[] formPair = data.split("=", 2);
        if (formPair.length == 2) {
            entity.put(formPair[0], formPair[1]);
            response.setHeader("X-Field-Set", formPair[0]);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
