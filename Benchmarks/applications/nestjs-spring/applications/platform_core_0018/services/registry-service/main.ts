import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RegisterService } from "./service_register";
import { MergeReport } from "./merge_report";
import { FormatReceipt } from "./format_receipt";
import { CollectSchedule } from "./collect_schedule";
import { SummarizeDigest } from "./summarize_digest";
import { RotateTenant } from "./rotate_tenant";
import { AnnotateWindow } from "./annotate_window";
import { CompactRoster } from "./compact_roster";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RegisterService, MergeReport, FormatReceipt, CollectSchedule, SummarizeDigest, RotateTenant, AnnotateWindow, CompactRoster],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
