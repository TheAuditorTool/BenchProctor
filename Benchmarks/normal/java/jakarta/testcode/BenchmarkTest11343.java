// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest11343 {

    @GET
    @Path("/BenchmarkTest11343")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest11343(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = "" + authHeader;
        try {
            Integer.parseInt(data);
        } catch (Exception ignored) {
        }
        return Response.ok("{\"status\":\"ok\"}", MediaType.APPLICATION_JSON).build();
    }
}
