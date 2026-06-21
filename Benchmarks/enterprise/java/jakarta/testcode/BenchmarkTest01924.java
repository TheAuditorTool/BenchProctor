// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest01924 {

    @GET
    @Path("/BenchmarkTest01924")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest01924(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        if (!new java.io.File("/var/app/data", new java.io.File(refererValue).getName()).delete()) { return Response.status(500).entity("delete failed").build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
