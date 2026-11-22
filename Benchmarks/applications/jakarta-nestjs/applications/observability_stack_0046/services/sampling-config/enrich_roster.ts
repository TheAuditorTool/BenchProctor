// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("sampling-config")
export class EnrichRoster {
  @Post("enrichRoster")
  async enrichRoster(@Req() req: Request): Promise<unknown> {
    const paragraph = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const gauge = Buffer.from(paragraph, "hex").toString();
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(gauge)) { throw new BadRequestException({error:"invalid"}); }
    const cohort = gauge;
    return new StreamableFile(Buffer.from("<section>" + cohort + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
