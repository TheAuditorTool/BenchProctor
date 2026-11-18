import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { CutRelease } from "./release_cut";
import { BuildPolicy } from "./build_policy";
import { ArchiveReport } from "./archive_report";
import { CollectDigest } from "./collect_digest";
import { ReconcileSchedule } from "./reconcile_schedule";
import { SummarizeReceipt } from "./summarize_receipt";
import { ExportCheckpoint } from "./export_checkpoint";
import { ResolveRelease } from "./resolve_release";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, CutRelease, BuildPolicy, ArchiveReport, CollectDigest, ReconcileSchedule, SummarizeReceipt, ExportCheckpoint, ResolveRelease],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
