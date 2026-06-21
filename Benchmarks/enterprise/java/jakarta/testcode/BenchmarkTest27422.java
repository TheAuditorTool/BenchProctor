// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest27422 {

    @POST
    @Path("/BenchmarkTest27422")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest27422(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        return Response.status(500).entity("Internal error").build();
    }
}
