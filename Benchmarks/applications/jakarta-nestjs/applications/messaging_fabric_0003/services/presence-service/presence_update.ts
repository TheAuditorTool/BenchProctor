// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("presence-service")
export class UpdatePresence {
  @Post("updatePresence")
  async updatePresence(@Req() req: Request): Promise<unknown> {
    const blurb = req.body.messaging_payload || "";
    await db.query("SELECT * FROM users WHERE id = $1", [blurb]);
    return { created: true };
  }
}
