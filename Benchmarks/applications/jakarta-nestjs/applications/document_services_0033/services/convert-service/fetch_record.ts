// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("convert-service")
export class FetchRecord {
  @Post("fetchRecord")
  async fetchRecord(@Req() req: Request): Promise<unknown> {
    const snippet = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const addendum = Buffer.from(snippet, "hex").toString();
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(addendum)) { throw new BadRequestException({error:"invalid"}); }
    const dossier = addendum;
    return new StreamableFile(Buffer.from("<section>" + dossier + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
