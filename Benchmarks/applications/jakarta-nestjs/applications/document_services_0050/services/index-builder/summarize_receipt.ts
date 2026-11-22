// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { DataSource } from "typeorm";

@Controller("index-builder")
export class SummarizeReceipt {
  @Post("summarizeReceipt")
  async summarizeReceipt(@Req() req: Request): Promise<unknown> {
    const citation = (req.body?.field as string) || "";
    const transform = (v: string): string => v.trim();
    const dossier: string = transform(citation);
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = '" + dossier + "'").getRawMany();
    return { created: true };
  }
}
