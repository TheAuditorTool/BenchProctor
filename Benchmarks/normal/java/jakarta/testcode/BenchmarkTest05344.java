// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest05344 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @POST
    @Path("/BenchmarkTest05344")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest05344(@Valid UserInput req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        FormData payload = new FormData(jsonValue);
        String data = payload.payload;
        String processed = org.owasp.encoder.Encode.forHtml(data);
        return Response.ok("<div>" + processed + "</div>", MediaType.TEXT_HTML).build();
    }
}
