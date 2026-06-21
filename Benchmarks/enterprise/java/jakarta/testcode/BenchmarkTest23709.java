// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest23709 {

    @GET
    @Path("/BenchmarkTest23709")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest23709(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(uaValue);
        String data = wrapper.toString();
        if ("admin".equals(data) || "ROLE_ADMIN".equals(data)) {
            return Response.ok("{\"status\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
        return Response.status(403).entity("forbidden").build();
    }
}
