// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest02465 {

    @GET
    @Path("/BenchmarkTest02465")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest02465(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = userId.isEmpty() ? "default" : userId;
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
