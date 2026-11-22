// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { DataSource } from "typeorm";

@Controller("bounce-handler")
export class RenderPolicy {
  @Post("renderPolicy")
  async renderPolicy(@Req() req: Request): Promise<unknown> {
    const preface = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const bulletin = preface != null ? preface : '';
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.query("SELECT * FROM users WHERE id = '" + bulletin + "'");
    return { created: true };
  }
}
