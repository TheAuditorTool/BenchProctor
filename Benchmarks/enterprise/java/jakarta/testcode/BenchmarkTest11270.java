// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest11270 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @GET
    @Path("/BenchmarkTest11270")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest11270(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = expandTabs(userId);
        if (!("true".equals(data) || "false".equals(data))) { return Response.status(400).build(); }
        jakarta.el.ELProcessor elp = new jakarta.el.ELProcessor();
        Object rendered = elp.eval(data);
        return Response.ok("<div>" + rendered + "</div>", MediaType.TEXT_HTML).build();
    }
}
