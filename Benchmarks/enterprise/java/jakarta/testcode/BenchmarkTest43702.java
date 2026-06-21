// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest43702 {

    private static String trimEnds(String v) { return v.trim(); }

    @GET
    @Path("/BenchmarkTest43702")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest43702(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = trimEnds(originValue);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            jakarta.el.ELProcessor elp = new jakarta.el.ELProcessor();
            Object rendered = elp.eval(data);
            return Response.ok("<div>" + rendered + "</div>", MediaType.TEXT_HTML).build();
        }
        return Response.ok().build();
    }
}
