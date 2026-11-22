import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { AttachAsset } from "./asset_attach";
import { ExportArticle } from "./export_article";
import { SummarizeSummary } from "./summarize_summary";
import { SummarizeRevision } from "./summarize_revision";
import { EnrichSchedule } from "./enrich_schedule";
import { MergeRevision } from "./merge_revision";
import { FormatIndex } from "./format_index";
import { FetchConfig } from "./fetch_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, AttachAsset, ExportArticle, SummarizeSummary, SummarizeRevision, EnrichSchedule, MergeRevision, FormatIndex, FetchConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
