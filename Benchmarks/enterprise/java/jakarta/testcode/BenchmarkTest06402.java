// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest06402 {

    @POST
    @Path("/BenchmarkTest06402")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest06402(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(rawData, "form");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
