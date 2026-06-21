// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest23798 {

    @GetMapping("/BenchmarkTest23798/{pathId}")
    public void BenchmarkTest23798(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String prefix = pathValue.length() > 0 ? pathValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = pathValue.toLowerCase(); break;
            case "f": data = pathValue.toUpperCase(); break;
            default: data = pathValue.strip(); break;
        }
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        request.setAttribute("hidden_form_field", data);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
