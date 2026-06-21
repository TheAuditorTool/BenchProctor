// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest10179 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @GET
    @Path("/BenchmarkTest10179")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest10179(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = collapseWhitespace(refererValue);
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            Object evalResult = new jakarta.el.ELProcessor().eval(data);
            response.setHeader("X-Eval-Result", String.valueOf(evalResult));
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
