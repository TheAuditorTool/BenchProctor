// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { DataSource } from "typeorm";
import { createClient } from "redis";

@Controller("index-builder")
export class BuildAttachment {
  @Post("buildAttachment")
  async buildAttachment(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const footnote = (await _cache.get("user_data")) || "";
    const addendum = Buffer.from(footnote, "base64").toString();
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.query("SELECT * FROM users WHERE id = '" + addendum + "'");
    return { created: true };
  }
}
