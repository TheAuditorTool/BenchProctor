// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("connector-api")
export class SummarizeRecord {
  @Post("summarizeRecord")
  async summarizeRecord(@Req() req: Request): Promise<unknown> {
    const heading = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const handshake = Buffer.from(heading, "hex").toString();
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(handshake)) { throw new BadRequestException({error:"invalid"}); }
    const remark = handshake;
    return new StreamableFile(Buffer.from("<section>" + remark + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
