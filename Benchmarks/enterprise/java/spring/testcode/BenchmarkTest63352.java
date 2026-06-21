// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest63352 {

    @PostMapping(path="/BenchmarkTest63352", consumes="multipart/form-data")
    public void BenchmarkTest63352(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data = uploadName.replace("\u0000", "");
        if (!String.valueOf(data).equals(request.getSession().getAttribute("csrfToken"))) {
            response.sendError(403, "csrf mismatch"); return;
        }
        String sessionRole = String.valueOf(request.getSession().getAttribute("role"));
        if (!"admin".equals(sessionRole)) { response.sendError(403, "forbidden"); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
