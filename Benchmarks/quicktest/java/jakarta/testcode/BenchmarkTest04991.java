// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest04991 {

    @GET
    @Path("/BenchmarkTest04991")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest04991(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = new String(java.util.Base64.getDecoder().decode(authHeader));
        String normalized = java.text.Normalizer.normalize(data, java.text.Normalizer.Form.NFKC);
        response.setContentType("text/html");
        return Response.ok("<p>" + normalized + "</p>", MediaType.TEXT_HTML).build();
    }
}
