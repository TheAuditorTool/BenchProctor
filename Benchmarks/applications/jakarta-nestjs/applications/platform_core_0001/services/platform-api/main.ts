import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ProvisionTenant } from "./tenant_provision";
import { ReconcileCheckpoint } from "./reconcile_checkpoint";
import { CompactQuota } from "./compact_quota";
import { RenderPolicy } from "./render_policy";
import { ValidateTenant } from "./validate_tenant";
import { ExportManifest } from "./export_manifest";
import { AnnotateReport } from "./annotate_report";
import { FetchLedger } from "./fetch_ledger";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ProvisionTenant, ReconcileCheckpoint, CompactQuota, RenderPolicy, ValidateTenant, ExportManifest, AnnotateReport, FetchLedger],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
