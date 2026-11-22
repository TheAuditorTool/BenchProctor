// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("index-builder")
export class SummarizeLedger {
  @Post("summarizeLedger")
  async summarizeLedger(@Req() req: Request): Promise<unknown> {
    const citation = process.env.DOCUMENTS_INPUT_0050 || "";
    const transform = (v: string): string => v.trim();
    const dossier: string = transform(citation);
    if (!/^(asc|desc|name|created)$/.test(String(dossier))) { throw new BadRequestException({error:"invalid"}); }
    const addendum = dossier;
    await db.query("SELECT * FROM users ORDER BY " + addendum);
    return { created: true };
  }
}
