import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SettleCapture } from "./capture_settle";
import { FormatReport } from "./format_report";
import { CollectHeader } from "./collect_header";
import { AnnotateManifest } from "./annotate_manifest";
import { FetchProfile } from "./fetch_profile";
import { ReconcileSummary } from "./reconcile_summary";
import { SummarizeProfile } from "./summarize_profile";
import { BuildHeader } from "./build_header";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SettleCapture, FormatReport, CollectHeader, AnnotateManifest, FetchProfile, ReconcileSummary, SummarizeProfile, BuildHeader],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
