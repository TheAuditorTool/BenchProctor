import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SearchKnowledge } from "./knowledge_search";
import { LoadReport } from "./load_report";
import { RotateRoster } from "./rotate_roster";
import { SummarizeCheckpoint } from "./summarize_checkpoint";
import { RotateSnapshot } from "./rotate_snapshot";
import { CollectSummary } from "./collect_summary";
import { EnrichDigest } from "./enrich_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SearchKnowledge, LoadReport, RotateRoster, SummarizeCheckpoint, RotateSnapshot, CollectSummary, EnrichDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
