// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { DataSource } from "typeorm";

@Controller("customs-service")
export class MergeCheckpoint {
  @Post("mergeCheckpoint")
  async mergeCheckpoint(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const consignment: string = transform(summary);
    const _coerced = parseInt(String(consignment), 10);
    const parcel = _coerced;
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.query("SELECT * FROM users WHERE id = '" + parcel + "'");
    return { created: true };
  }
}
