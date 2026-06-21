// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest47899 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @GET
    @Path("/BenchmarkTest47899")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest47899(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        FormData payload = new FormData(originValue);
        String data = payload.payload;
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
