// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest38302 {

    @GET
    @Path("/BenchmarkTest38302")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest38302(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        response.setContentType("text/html");
        return Response.ok(originValue, MediaType.TEXT_HTML).build();
    }
}
