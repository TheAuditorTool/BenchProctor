import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ConfigureSample } from "./sample_config";
import { CollectSnapshot } from "./collect_snapshot";
import { ResolveSummary } from "./resolve_summary";
import { FetchWindow } from "./fetch_window";
import { FetchConfig } from "./fetch_config";
import { CompactPolicy } from "./compact_policy";
import { SummarizeSnapshot } from "./summarize_snapshot";
import { ArchiveSummary } from "./archive_summary";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ConfigureSample, CollectSnapshot, ResolveSummary, FetchWindow, FetchConfig, CompactPolicy, SummarizeSnapshot, ArchiveSummary],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
