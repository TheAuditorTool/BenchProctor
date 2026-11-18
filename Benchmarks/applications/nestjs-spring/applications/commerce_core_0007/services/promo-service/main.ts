import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ApplyPromo } from "./promo_apply";
import { LoadWindow } from "./load_window";
import { CollectManifest } from "./collect_manifest";
import { FetchSummary } from "./fetch_summary";
import { RenderReport } from "./render_report";
import { AuditLedger } from "./audit_ledger";
import { PublishSchedule } from "./publish_schedule";
import { FetchBatch } from "./fetch_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ApplyPromo, LoadWindow, CollectManifest, FetchSummary, RenderReport, AuditLedger, PublishSchedule, FetchBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
