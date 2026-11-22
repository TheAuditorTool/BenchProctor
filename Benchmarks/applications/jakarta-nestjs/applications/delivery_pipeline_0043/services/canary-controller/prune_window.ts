// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("canary-controller")
export class PruneWindow {
  @Post("pruneWindow")
  async pruneWindow(@Req() req: Request): Promise<unknown> {
    const remark = (req.query.id as string) || "";
    const note = Buffer.from(remark, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [note]);
    return { created: true };
  }
}
