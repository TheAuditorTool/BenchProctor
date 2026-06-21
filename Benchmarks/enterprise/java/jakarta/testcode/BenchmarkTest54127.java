// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest54127 {

    @GET
    @Path("/BenchmarkTest54127")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest54127(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(userId, "request");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
