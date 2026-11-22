import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { PushSyndication } from "./syndication_push";
import { AnnotateIndex } from "./annotate_index";
import { PruneSyndication } from "./prune_syndication";
import { ReconcileWindow } from "./reconcile_window";
import { SummarizeConfig } from "./summarize_config";
import { FormatCheckpoint } from "./format_checkpoint";
import { FetchSummary } from "./fetch_summary";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PushSyndication, AnnotateIndex, PruneSyndication, ReconcileWindow, SummarizeConfig, FormatCheckpoint, FetchSummary],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
