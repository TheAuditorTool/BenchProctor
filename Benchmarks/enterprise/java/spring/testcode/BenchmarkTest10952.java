// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10952 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @PostMapping("/BenchmarkTest10952")
    public void BenchmarkTest10952(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        FormData payload = new FormData(commentValue);
        String data = payload.payload;
        response.sendError(500, data);
    }
}
