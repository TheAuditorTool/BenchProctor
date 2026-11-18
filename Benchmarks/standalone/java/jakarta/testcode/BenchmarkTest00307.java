// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.container.ContainerRequestContext;
import jakarta.ws.rs.container.ContainerRequestFilter;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00307 {

    @Provider
    public static class BindingRestrictionFilter implements ContainerRequestFilter {
        @Override
        public void filter(ContainerRequestContext requestContext) {
            requestContext.getHeaders().remove("X-Internal-Bind");
        }
    }

    @Provider
    public static class FailureMapper implements ExceptionMapper<Exception> {
        @Override
        public Response toResponse(Exception ex) {
            return Response.status(500).entity("request failed").build();
        }
    }

    @GET
    @Path("/BenchmarkTest00307")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00307(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(userId, "query");
        String data = entry.getKey();
        if (!data.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { return Response.status(400).build(); }
        java.util.Hashtable<String,String> env = new java.util.Hashtable<>();
        env.put(javax.naming.Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");
        env.put(javax.naming.Context.PROVIDER_URL, System.getenv().getOrDefault("LDAP_URL", "ldap://directory:1389"));
        javax.naming.directory.DirContext ctx = new javax.naming.directory.InitialDirContext(env);
        try {
            ctx.search("ou=people,dc=example,dc=com", "(uid=" + data + ")", new javax.naming.directory.SearchControls());
        } finally { ctx.close(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
