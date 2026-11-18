import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { DispatchCarrier } from "./carrier_dispatch";
import { SummarizeSnapshot } from "./summarize_snapshot";
import { ReconcileManifest } from "./reconcile_manifest";
import { ResolveRecord } from "./resolve_record";
import { ExportRecord } from "./export_record";
import { ArchiveRoster } from "./archive_roster";
import { BuildThreshold } from "./build_threshold";
import { AuditReceipt } from "./audit_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, DispatchCarrier, SummarizeSnapshot, ReconcileManifest, ResolveRecord, ExportRecord, ArchiveRoster, BuildThreshold, AuditReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
