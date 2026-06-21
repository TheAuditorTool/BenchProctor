// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest72210 {

    @PostMapping(path="/BenchmarkTest72210", consumes="multipart/form-data")
    public void BenchmarkTest72210(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(uploadName, "form");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        request.setAttribute("hidden_form_field", data);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
