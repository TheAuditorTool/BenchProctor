// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest41261 {

    @GET
    @Path("/BenchmarkTest41261")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest41261(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String prefix = userId.length() > 0 ? userId.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = userId.toLowerCase(); break;
            case "f": data = userId.toUpperCase(); break;
            default: data = userId.strip(); break;
        }
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + data + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
