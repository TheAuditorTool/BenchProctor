// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest38071 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest38071")
    public void BenchmarkTest38071(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = normalize(authHeader);
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
