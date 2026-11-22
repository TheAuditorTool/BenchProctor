import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { CutRelease } from "./release_cut";
import { PublishSnapshot } from "./publish_snapshot";
import { MergeWindow } from "./merge_window";
import { BuildSummary } from "./build_summary";
import { MergeCanary } from "./merge_canary";
import { NormalizeConfig } from "./normalize_config";
import { FormatSummary } from "./format_summary";
import { ExportReport } from "./export_report";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, CutRelease, PublishSnapshot, MergeWindow, BuildSummary, MergeCanary, NormalizeConfig, FormatSummary, ExportReport],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
