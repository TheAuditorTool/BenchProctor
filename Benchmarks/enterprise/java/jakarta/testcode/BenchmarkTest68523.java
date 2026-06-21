// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest68523 {

    @GET
    @Path("/BenchmarkTest68523/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest68523(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(pathValue, "query");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        return Response.ok("<input type=\"text\" name=\"q\" value=\"" + data + "\">", MediaType.TEXT_HTML).build();
    }
}
