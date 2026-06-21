// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest58461 {

    @GET
    @Path("/BenchmarkTest58461")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest58461(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String prefix = authHeader.length() > 0 ? authHeader.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = authHeader.toLowerCase(); break;
            case "f": data = authHeader.toUpperCase(); break;
            default: data = authHeader.strip(); break;
        }
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
