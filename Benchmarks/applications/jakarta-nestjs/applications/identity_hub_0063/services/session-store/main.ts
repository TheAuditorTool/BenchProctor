import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { CreateSession } from "./session_create";
import { AnnotateSnapshot } from "./annotate_snapshot";
import { CompactDigest } from "./compact_digest";
import { AuditSummary } from "./audit_summary";
import { RenderLedger } from "./render_ledger";
import { FormatCheckpoint } from "./format_checkpoint";
import { EnrichSession } from "./enrich_session";
import { EnrichReceipt } from "./enrich_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, CreateSession, AnnotateSnapshot, CompactDigest, AuditSummary, RenderLedger, FormatCheckpoint, EnrichSession, EnrichReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
