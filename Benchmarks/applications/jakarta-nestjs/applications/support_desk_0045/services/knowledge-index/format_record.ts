// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { DataSource } from "typeorm";

@Controller("knowledge-index")
export class FormatRecord {
  @Post("formatRecord")
  async formatRecord(@Req() req: Request): Promise<unknown> {
    const remark = (req.body.field as string) || "";
    const transform = (v: string): string => v.trim();
    const inquiry: string = transform(remark);
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = '" + inquiry + "'").getRawMany();
    return { created: true };
  }
}
