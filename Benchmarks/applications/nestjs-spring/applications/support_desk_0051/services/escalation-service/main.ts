import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RaiseEscalation } from "./escalation_raise";
import { ResolveConfig } from "./resolve_config";
import { PruneReport } from "./prune_report";
import { NormalizeProfile } from "./normalize_profile";
import { ReconcileIndex } from "./reconcile_index";
import { ResolveIndex } from "./resolve_index";
import { AuditBundle } from "./audit_bundle";
import { EnrichConfig } from "./enrich_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RaiseEscalation, ResolveConfig, PruneReport, NormalizeProfile, ReconcileIndex, ResolveIndex, AuditBundle, EnrichConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
