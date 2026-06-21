// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest82479 {

    @GET
    @Path("/BenchmarkTest82479/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest82479(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = String.format("%s", pathValue);
        jakarta.el.ELProcessor elp = new jakarta.el.ELProcessor();
        Object rendered = elp.eval(data);
        return Response.ok("<div>" + rendered + "</div>", MediaType.TEXT_HTML).build();
    }
}
