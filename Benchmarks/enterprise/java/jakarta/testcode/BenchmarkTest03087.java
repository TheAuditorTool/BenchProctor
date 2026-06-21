// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest03087 {

    @GET
    @Path("/BenchmarkTest03087")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest03087(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        return Response.ok("<div>" + userId + "</div>", MediaType.TEXT_HTML).build();
    }
}
