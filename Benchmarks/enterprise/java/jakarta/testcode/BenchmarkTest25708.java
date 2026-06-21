// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest25708 {

    @GET
    @Path("/BenchmarkTest25708")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest25708(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        return Response.ok("<div>" + userId + "</div>", MediaType.TEXT_HTML).build();
    }
}
