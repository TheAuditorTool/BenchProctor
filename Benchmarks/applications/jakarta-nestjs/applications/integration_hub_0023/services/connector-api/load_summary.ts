// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("connector-api")
export class LoadSummary {
  @Post("loadSummary")
  async loadSummary(@Req() req: Request): Promise<unknown> {
    const caption = (req.query.id as string) || "";
    const handshake = Buffer.from(caption, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [handshake]);
    return { created: true };
  }
}
