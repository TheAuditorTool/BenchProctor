// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest74531 {

    @GET
    @Path("/BenchmarkTest74531/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest74531(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        if ("https://app.acmecdn.net".equals(pathValue)) response.setHeader("Access-Control-Allow-Origin", pathValue);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
