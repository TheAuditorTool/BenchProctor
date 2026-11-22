// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("consent-registry")
export class BuildWindow {
  @Post("buildWindow")
  async buildWindow(@Req() req: Request): Promise<unknown> {
    const remark = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const persona = Buffer.from(remark, "hex").toString();
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(persona)) { throw new BadRequestException({error:"invalid"}); }
    const notice = persona;
    return new StreamableFile(Buffer.from("<section>" + notice + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
