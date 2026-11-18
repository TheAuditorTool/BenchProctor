// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { escapeIdentifier } from "pg";

@Controller("knowledge-index")
export class SummarizeDigest {
  @Post("summarizeDigest")
  async summarizeDigest(@Req() req: Request): Promise<unknown> {
    const citation = (req.body as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(citation);
    const grievance: string = readInput();
    await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(grievance)));
    return { created: true };
  }
}
