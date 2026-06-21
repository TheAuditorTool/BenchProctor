// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest34369 {

    @GET
    @Path("/BenchmarkTest34369")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest34369(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        Integer.parseInt(authHeader);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
