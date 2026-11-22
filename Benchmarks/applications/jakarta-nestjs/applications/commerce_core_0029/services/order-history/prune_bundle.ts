// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("order-history")
export class PruneBundle {
  @Post("pruneBundle")
  async pruneBundle(@Req() req: Request): Promise<unknown> {
    const notice = (req.query.id as string) || "";
    const backorder = Buffer.from(notice, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [backorder]);
    return { created: true };
  }
}
