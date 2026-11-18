// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { DataSource } from "typeorm";

@Controller("presence-hub")
export class BuildDocument {
  @Post("buildDocument")
  async buildDocument(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.authorization as string) || "";
    const tokens = String(preface).split(',').filter((t) => t.length > 0);
    const remark = tokens.join(' ');
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.query("SELECT * FROM users WHERE id = $1", [remark]);
    return { created: true };
  }
}
