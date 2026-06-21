// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest10644 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @POST
    @Path("/BenchmarkTest10644")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest10644(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        FormData payload = new FormData(xmlValue);
        String data = payload.payload;
        response.setContentType("text/html");
        return Response.ok(data, MediaType.TEXT_HTML).build();
    }
}
