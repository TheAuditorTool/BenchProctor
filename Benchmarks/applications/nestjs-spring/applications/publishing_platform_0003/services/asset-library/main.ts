import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { AttachAsset } from "./asset_attach";
import { MergeConfig } from "./merge_config";
import { ValidateWindow } from "./validate_window";
import { SummarizeConfig } from "./summarize_config";
import { FetchThreshold } from "./fetch_threshold";
import { RenderReport } from "./render_report";
import { VerifySnapshot } from "./verify_snapshot";
import { CollectWindow } from "./collect_window";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, AttachAsset, MergeConfig, ValidateWindow, SummarizeConfig, FetchThreshold, RenderReport, VerifySnapshot, CollectWindow],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
