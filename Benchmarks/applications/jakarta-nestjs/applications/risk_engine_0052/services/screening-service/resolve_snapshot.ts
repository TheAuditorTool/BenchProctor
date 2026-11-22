// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("screening-service")
export class ResolveSnapshot {
  @Post("resolveSnapshot")
  async resolveSnapshot(@Req() req: Request): Promise<unknown> {
    const memo = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const verdict = Buffer.from(memo, "hex").toString();
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(verdict)) { throw new BadRequestException({error:"invalid"}); }
    const grievance = verdict;
    return new StreamableFile(Buffer.from("<section>" + grievance + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
