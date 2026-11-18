// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("returns-service")
export class CompactRecord {
  @Post("compactRecord/:id")
  async compactRecord(@Req() req: Request): Promise<unknown> {
    const citation = (req.params.id as string) || "";
    const backorder = citation != null ? citation : '';
    await db.query("SELECT * FROM users WHERE id = $1", [backorder]);
    return { created: true };
  }
}
