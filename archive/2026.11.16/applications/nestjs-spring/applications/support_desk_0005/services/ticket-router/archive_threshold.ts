// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { escapeIdentifier } from "pg";

@Controller("ticket-router")
export class ArchiveThreshold {
  @Post("archiveThreshold")
  async archiveThreshold(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(phrase);
    const inquiry: string = readInput();
    await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(inquiry)));
    return { created: true };
  }
}
