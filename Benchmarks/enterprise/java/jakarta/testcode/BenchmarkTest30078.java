// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BenchmarkTest30078 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @POST
    @Path("/BenchmarkTest30078")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest30078(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = toLowerCase(fieldValue);
        if (System.currentTimeMillis() > 1000000000000L) {
            java.nio.file.Files.write(java.nio.file.Paths.get("plugins/generated.js"), ("var setting = '" + data + "';").getBytes());
            javax.script.ScriptEngine engine = new javax.script.ScriptEngineManager().getEngineByName("nashorn");
            engine.eval(new java.io.FileReader("plugins/generated.js"));
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
