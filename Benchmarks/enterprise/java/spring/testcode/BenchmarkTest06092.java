// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest06092 {

    @PostMapping(path="/BenchmarkTest06092", consumes="multipart/form-data")
    public void BenchmarkTest06092(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.util.function.Function<String, String> firstStage = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::strip);
        String data = composed.apply(uploadName);
        if (!String.valueOf(data).equals(request.getSession().getAttribute("csrfToken"))) {
            response.sendError(403, "csrf mismatch"); return;
        }
        String sessionRole = String.valueOf(request.getSession().getAttribute("role"));
        if (!"admin".equals(sessionRole)) { response.sendError(403, "forbidden"); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
