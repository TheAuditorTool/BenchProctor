import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { MintToken } from "./token_mint";
import { CompactIndex } from "./compact_index";
import { SummarizeSummary } from "./summarize_summary";
import { FormatReport } from "./format_report";
import { BuildBatch } from "./build_batch";
import { NormalizeHeader } from "./normalize_header";
import { CompactConsent } from "./compact_consent";
import { RenderReceipt } from "./render_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, MintToken, CompactIndex, SummarizeSummary, FormatReport, BuildBatch, NormalizeHeader, CompactConsent, RenderReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
