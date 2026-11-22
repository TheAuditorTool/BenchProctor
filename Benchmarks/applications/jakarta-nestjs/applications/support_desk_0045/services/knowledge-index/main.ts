import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SearchKnowledge } from "./knowledge_search";
import { SummarizeReceipt } from "./summarize_receipt";
import { FormatRecord } from "./format_record";
import { SummarizeCheckpoint } from "./summarize_checkpoint";
import { EnrichThreshold } from "./enrich_threshold";
import { LoadLedger } from "./load_ledger";
import { RenderTicket } from "./render_ticket";
import { FetchWindow } from "./fetch_window";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SearchKnowledge, SummarizeReceipt, FormatRecord, SummarizeCheckpoint, EnrichThreshold, LoadLedger, RenderTicket, FetchWindow],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
