// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("platform-api")
export class VerifyDigest {
  @Post("verifyDigest")
  async verifyDigest(@Req() req: Request): Promise<unknown> {
    const note = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const handshake = Buffer.from(note, "base64").toString();
    return "<div>" + handshake + "</div>";
  }
}
