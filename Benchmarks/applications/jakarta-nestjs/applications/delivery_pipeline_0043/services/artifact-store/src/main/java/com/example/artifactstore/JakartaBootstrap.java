package com.example.artifactstore;

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
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.artifactstore.JakartaBootstrap$HealthResource,com.example.artifactstore.AnnotateWindow,com.example.artifactstore.ArchiveSummary,com.example.artifactstore.CompactPolicy,com.example.artifactstore.LoadSummary,com.example.artifactstore.PruneReport,com.example.artifactstore.PublishArtifact,com.example.artifactstore.SummarizeReport,com.example.artifactstore.VerifyHeader");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
