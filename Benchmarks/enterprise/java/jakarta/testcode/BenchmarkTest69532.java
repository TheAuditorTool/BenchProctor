// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest69532 {

    @GET
    @Path("/BenchmarkTest69532")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest69532(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String prefix = refererValue.length() > 0 ? refererValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = refererValue.toLowerCase(); break;
            case "f": data = refererValue.toUpperCase(); break;
            default: data = refererValue.strip(); break;
        }
        String normalized = java.text.Normalizer.normalize(data, java.text.Normalizer.Form.NFKC);
        response.setContentType("text/html");
        return Response.ok("<p>" + normalized + "</p>", MediaType.TEXT_HTML).build();
    }
}
