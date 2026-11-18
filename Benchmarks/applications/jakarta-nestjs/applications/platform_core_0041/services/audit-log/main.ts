import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { AppendAudit } from "./audit_append";
import { LoadHeader } from "./load_header";
import { CompactFlag } from "./compact_flag";
import { ExportFlag } from "./export_flag";
import { ResolveIndex } from "./resolve_index";
import { AnnotateSecret } from "./annotate_secret";
import { FetchSummary } from "./fetch_summary";
import { BuildIndex } from "./build_index";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, AppendAudit, LoadHeader, CompactFlag, ExportFlag, ResolveIndex, AnnotateSecret, FetchSummary, BuildIndex],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
