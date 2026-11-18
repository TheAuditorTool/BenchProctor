import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { PublishMessage } from "./message_publish";
import { AnnotateRoster } from "./annotate_roster";
import { SummarizeBundle } from "./summarize_bundle";
import { ResolveBatch } from "./resolve_batch";
import { PruneReport } from "./prune_report";
import { LoadLedger } from "./load_ledger";
import { SummarizeManifest } from "./summarize_manifest";
import { ReconcileSchedule } from "./reconcile_schedule";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PublishMessage, AnnotateRoster, SummarizeBundle, ResolveBatch, PruneReport, LoadLedger, SummarizeManifest, ReconcileSchedule],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
