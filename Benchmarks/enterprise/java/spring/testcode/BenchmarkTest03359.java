// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03359 {

    @GetMapping("/BenchmarkTest03359")
    public void BenchmarkTest03359(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String prefix = userId.length() > 0 ? userId.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = userId.toLowerCase(); break;
            case "f": data = userId.toUpperCase(); break;
            default: data = userId.strip(); break;
        }
        int result = 100 / Integer.parseInt(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
