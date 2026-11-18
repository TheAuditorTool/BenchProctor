// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { DataSource } from "typeorm";
import { createClient } from "redis";

@Controller("knowledge-index")
export class ArchiveSurvey {
  @Post("archiveSurvey")
  async archiveSurvey(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const citation = (await _cache.get("user_data")) || "";
    const grievance = citation != null ? citation : '';
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.query("SELECT * FROM users WHERE id = '" + grievance + "'");
    return { created: true };
  }
}
