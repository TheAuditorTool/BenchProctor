// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest26394 {

    @GET
    @Path("/BenchmarkTest26394")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest26394(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = String.format("payload=%s", hostValue);
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        String normalized = java.text.Normalizer.normalize(data, java.text.Normalizer.Form.NFKC);
        response.setContentType("text/html");
        return Response.ok("<p>" + normalized + "</p>", MediaType.TEXT_HTML).build();
    }
}
