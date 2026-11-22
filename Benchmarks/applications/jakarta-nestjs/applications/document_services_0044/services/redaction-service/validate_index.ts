// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("redaction-service")
export class ValidateIndex {
  @Post("validateIndex")
  async validateIndex(@Req() req: Request): Promise<unknown> {
    const phrase = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const dossier = Buffer.from(phrase, "hex").toString();
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(dossier)) { throw new BadRequestException({error:"invalid"}); }
    const addendum = dossier;
    return new StreamableFile(Buffer.from("<section>" + addendum + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
