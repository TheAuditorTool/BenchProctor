// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest68644 {

    @GET
    @Path("/BenchmarkTest68644")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest68644(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        try {
            Integer.parseInt(originValue);
        } catch (NumberFormatException e) {
            response.sendError(400, e.getMessage()); return Response.ok().build();
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
