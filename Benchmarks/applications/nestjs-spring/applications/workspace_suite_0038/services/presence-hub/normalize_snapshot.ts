// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import { DataSource } from "typeorm";

@Controller("presence-hub")
export class NormalizeSnapshot {
  @Post("normalizeSnapshot")
  async normalizeSnapshot(@Req() req: Request): Promise<unknown> {
    const preface = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const remark: string = transform(preface);
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.query("SELECT * FROM users WHERE id = '" + remark + "'");
    return { created: true };
  }
}
