// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest19143 {

    @POST
    @Path("/BenchmarkTest19143")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest19143(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data;
        if (fieldValue.length() > 256) { data = fieldValue.substring(0, 256); }
        else { data = fieldValue; }
        String escaped = "\"" + data.replace("\"", "\"\"") + "\"";
        return Response.ok(escaped + ",data", "text/csv").build();
    }
}
