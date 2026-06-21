// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06565 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest06565")
    public void BenchmarkTest06565(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = stripWhitespace(userId);
        if (data.length() > 2048) { response.sendError(400, "schema invalid"); return; }
        new Socket(data, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
