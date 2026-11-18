import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ApplyRedaction } from "./redaction_apply";
import { CompactIndex } from "./compact_index";
import { CompactDigest } from "./compact_digest";
import { PublishSummary } from "./publish_summary";
import { ReconcileIndex } from "./reconcile_index";
import { SummarizeRecord } from "./summarize_record";
import { FetchConfig } from "./fetch_config";
import { FetchIndex } from "./fetch_index";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ApplyRedaction, CompactIndex, CompactDigest, PublishSummary, ReconcileIndex, SummarizeRecord, FetchConfig, FetchIndex],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
