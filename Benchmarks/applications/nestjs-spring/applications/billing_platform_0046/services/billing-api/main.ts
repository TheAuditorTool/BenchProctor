import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SubmitInvoice } from "./invoice_intake";
import { ArchiveRecord } from "./archive_record";
import { LoadRoster } from "./load_roster";
import { ResolveProfile } from "./resolve_profile";
import { PruneProfile } from "./prune_profile";
import { AnnotateWindow } from "./annotate_window";
import { NormalizeIndex } from "./normalize_index";
import { PruneRecord } from "./prune_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SubmitInvoice, ArchiveRecord, LoadRoster, ResolveProfile, PruneProfile, AnnotateWindow, NormalizeIndex, PruneRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
