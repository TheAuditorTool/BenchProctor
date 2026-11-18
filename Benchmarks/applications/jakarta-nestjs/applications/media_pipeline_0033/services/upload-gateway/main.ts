import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { UploadAsset } from "./asset_upload";
import { AuditConfig } from "./audit_config";
import { NormalizeReport } from "./normalize_report";
import { EnrichReport } from "./enrich_report";
import { RenderSnapshot } from "./render_snapshot";
import { LoadLedger } from "./load_ledger";
import { PruneSnapshot } from "./prune_snapshot";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, UploadAsset, AuditConfig, NormalizeReport, EnrichReport, RenderSnapshot, LoadLedger, PruneSnapshot],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
