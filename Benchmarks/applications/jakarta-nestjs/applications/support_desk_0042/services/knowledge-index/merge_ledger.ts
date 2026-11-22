// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("knowledge-index")
export class MergeLedger {
  @Post("mergeLedger")
  async mergeLedger(@Req() req: Request): Promise<unknown> {
    const blurb = (req.query.id as string) || "";
    const inquiry = Buffer.from(blurb, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [inquiry]);
    return { created: true };
  }
}
