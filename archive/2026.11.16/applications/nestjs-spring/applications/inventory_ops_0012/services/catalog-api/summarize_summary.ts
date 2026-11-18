// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { escapeIdentifier } from "pg";

@Controller("catalog-api")
export class SummarizeSummary {
  @Post("summarizeSummary")
  async summarizeSummary(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(phrase);
    const backorder: string = readInput();
    await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(backorder)));
    return { created: true };
  }
}
