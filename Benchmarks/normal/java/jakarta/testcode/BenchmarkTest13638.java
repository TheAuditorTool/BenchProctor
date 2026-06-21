// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest13638 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @GET
    @Path("/BenchmarkTest13638")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest13638(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = toLowerCase(authHeader);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            Object evaluated = new jakarta.el.ELProcessor().eval(data);
            return Response.ok("<div>" + evaluated + "</div>", MediaType.TEXT_HTML).build();
        }
        return Response.ok().build();
    }
}
