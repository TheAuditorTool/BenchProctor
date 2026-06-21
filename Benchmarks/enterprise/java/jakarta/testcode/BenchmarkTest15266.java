// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest15266 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @GET
    @Path("/BenchmarkTest15266")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest15266(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = expandTabs(originValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        String[] values = processed.split(",");
        if (values.length > 0) {
            response.setHeader("X-Param-First", values[0]);
            response.setHeader("X-Param-Dropped", String.valueOf(values.length - 1));
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
