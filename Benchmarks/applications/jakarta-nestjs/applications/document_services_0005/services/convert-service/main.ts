import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RunConversion } from "./convert_job";
import { BuildRoster } from "./build_roster";
import { PublishHeader } from "./publish_header";
import { CompactConfig } from "./compact_config";
import { FormatSchedule } from "./format_schedule";
import { CompactSignature } from "./compact_signature";
import { CollectBatch } from "./collect_batch";
import { SummarizeThreshold } from "./summarize_threshold";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RunConversion, BuildRoster, PublishHeader, CompactConfig, FormatSchedule, CompactSignature, CollectBatch, SummarizeThreshold],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
