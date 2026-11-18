import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SearchKnowledge } from "./knowledge_search";
import { ArchiveSurvey } from "./archive_survey";
import { RenderThreshold } from "./render_threshold";
import { AnnotateMacro } from "./annotate_macro";
import { ArchiveSnapshot } from "./archive_snapshot";
import { ArchiveTicket } from "./archive_ticket";
import { SummarizeDigest } from "./summarize_digest";
import { ReconcileLedger } from "./reconcile_ledger";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SearchKnowledge, ArchiveSurvey, RenderThreshold, AnnotateMacro, ArchiveSnapshot, ArchiveTicket, SummarizeDigest, ReconcileLedger],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
