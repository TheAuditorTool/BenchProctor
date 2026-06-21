// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest75415 {

    @GET
    @Path("/BenchmarkTest75415")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest75415(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(refererValue, "request");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
