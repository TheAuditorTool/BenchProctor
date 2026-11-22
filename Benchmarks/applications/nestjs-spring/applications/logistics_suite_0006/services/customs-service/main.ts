import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { DeclareCustoms } from "./customs_declare";
import { RenderSummary } from "./render_summary";
import { PruneSchedule } from "./prune_schedule";
import { AuditConfig } from "./audit_config";
import { AnnotateHeader } from "./annotate_header";
import { ExportCheckpoint } from "./export_checkpoint";
import { MergeCheckpoint } from "./merge_checkpoint";
import { BuildWaybill } from "./build_waybill";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, DeclareCustoms, RenderSummary, PruneSchedule, AuditConfig, AnnotateHeader, ExportCheckpoint, MergeCheckpoint, BuildWaybill],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
