// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09894 {

    private enum AllowedValue { PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED }

    @GetMapping("/BenchmarkTest09894")
    public void BenchmarkTest09894(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : userId.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        java.util.HashMap<String,Object> entity = new java.util.HashMap<>();
        String[] kv = data.split("=", 2);
        if (kv.length == 2) {
            entity.put(kv[0], kv[1]);
            response.setHeader("X-Field-Set", kv[0]);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
