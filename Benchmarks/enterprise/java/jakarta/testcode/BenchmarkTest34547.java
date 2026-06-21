// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest34547 {

    @GET
    @Path("/BenchmarkTest34547")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest34547(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(forwardedIp, "query");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        Object evalResult = new jakarta.el.ELProcessor().eval(data);
        response.setHeader("X-Eval-Result", String.valueOf(evalResult));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
