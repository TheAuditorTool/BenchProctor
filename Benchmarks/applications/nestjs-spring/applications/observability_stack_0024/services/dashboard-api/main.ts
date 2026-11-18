import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { QueryDashboard } from "./dashboard_query";
import { PruneLedger } from "./prune_ledger";
import { ResolveHeader } from "./resolve_header";
import { EnrichIndex } from "./enrich_index";
import { CollectBundle } from "./collect_bundle";
import { CollectReport } from "./collect_report";
import { AnnotateRecord } from "./annotate_record";
import { FormatDigest } from "./format_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, QueryDashboard, PruneLedger, ResolveHeader, EnrichIndex, CollectBundle, CollectReport, AnnotateRecord, FormatDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
