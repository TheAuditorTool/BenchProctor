import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { BuildChangelog } from "./changelog_build";
import { PruneIndex } from "./prune_index";
import { CollectDigest } from "./collect_digest";
import { ReconcileSchedule } from "./reconcile_schedule";
import { SummarizeReceipt } from "./summarize_receipt";
import { ExportCheckpoint } from "./export_checkpoint";
import { ResolveRelease } from "./resolve_release";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, BuildChangelog, PruneIndex, CollectDigest, ReconcileSchedule, SummarizeReceipt, ExportCheckpoint, ResolveRelease],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
