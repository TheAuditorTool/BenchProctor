package com.example.escalationservice;

public class JakartaBootstrap {

    @jakarta.ws.rs.Path("/health")
    public static class HealthResource {
        @jakarta.ws.rs.GET
        public jakarta.ws.rs.core.Response health() {
            return jakarta.ws.rs.core.Response.ok("ok").build();
        }
    }

    public static void main(String[] args) throws Exception {
        java.util.Map<String, String> initParams = new java.util.HashMap<>();
        initParams.put(
            "jersey.config.server.provider.classnames",
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.escalationservice.JakartaBootstrap$HealthResource,com.example.escalationservice.ArchiveSurvey,com.example.escalationservice.ExportManifest,com.example.escalationservice.LoadReceipt,com.example.escalationservice.MergeWindow,com.example.escalationservice.PruneReport,com.example.escalationservice.RaiseEscalation,com.example.escalationservice.ResolveConfig,com.example.escalationservice.ResolveWindow");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
