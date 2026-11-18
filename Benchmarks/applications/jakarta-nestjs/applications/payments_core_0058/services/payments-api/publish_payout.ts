// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("payments-api")
export class PublishPayout {
  @Post("publishPayout")
  async publishPayout(@Req() req: Request): Promise<unknown> {
    const caption = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const ledger = Buffer.from(caption, "base64").toString();
    return "<div>" + ledger + "</div>";
  }
}
