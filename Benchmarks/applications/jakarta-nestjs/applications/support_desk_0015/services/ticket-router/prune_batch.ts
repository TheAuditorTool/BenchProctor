// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("ticket-router")
export class PruneBatch {
  @Post("pruneBatch")
  async pruneBatch(@Req() req: Request): Promise<unknown> {
    const phrase = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const grievance = Buffer.from(phrase, "hex").toString();
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(grievance)) { throw new BadRequestException({error:"invalid"}); }
    const inquiry = grievance;
    return new StreamableFile(Buffer.from("<section>" + inquiry + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
