import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RecordBounce } from "./bounce_record";
import { CompactLedger } from "./compact_ledger";
import { RenderReport } from "./render_report";
import { EnrichHeader } from "./enrich_header";
import { FormatCheckpoint } from "./format_checkpoint";
import { PublishSchedule } from "./publish_schedule";
import { SummarizeSchedule } from "./summarize_schedule";
import { AuditMessage } from "./audit_message";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RecordBounce, CompactLedger, RenderReport, EnrichHeader, FormatCheckpoint, PublishSchedule, SummarizeSchedule, AuditMessage],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
