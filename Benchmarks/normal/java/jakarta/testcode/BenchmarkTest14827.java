// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest14827 {

    @GET
    @Path("/BenchmarkTest14827")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest14827(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        return Response.ok("<div>" + authHeader + "</div>", MediaType.TEXT_HTML).build();
    }
}
