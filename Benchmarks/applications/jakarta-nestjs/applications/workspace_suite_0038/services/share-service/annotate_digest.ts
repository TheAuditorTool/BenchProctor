// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import knex from "knex";

@Controller("share-service")
export class AnnotateDigest {
  @Post("annotateDigest")
  async annotateDigest(@Req() req: Request): Promise<unknown> {
    const preface = (req.body as string) || "";
    let remark;
    try { remark = JSON.parse(preface).value || ""; }
    catch (e) { remark = String(preface); }
    const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    await _knex.raw("SELECT * FROM users WHERE id = '" + remark + "'");
    return { created: true };
  }
}
