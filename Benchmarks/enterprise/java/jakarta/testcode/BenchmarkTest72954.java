// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest72954 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @GET
    @Path("/BenchmarkTest72954/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest72954(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        FormData payload = new FormData(pathValue);
        String data = payload.payload;
        return Response.status(500).entity(data).build();
    }
}
