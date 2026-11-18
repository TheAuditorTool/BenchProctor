import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { TriggerRollback } from "./rollback_trigger";
import { LoadRoster } from "./load_roster";
import { SummarizeRelease } from "./summarize_release";
import { VerifyReceipt } from "./verify_receipt";
import { ExportArtifact } from "./export_artifact";
import { VerifyCheckpoint } from "./verify_checkpoint";
import { FetchRoster } from "./fetch_roster";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, TriggerRollback, LoadRoster, SummarizeRelease, VerifyReceipt, ExportArtifact, VerifyCheckpoint, FetchRoster],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
