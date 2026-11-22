// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("asset-library")
export class SummarizeRevision {
  @Post("summarizeRevision")
  async summarizeRevision(@Req() req: Request): Promise<unknown> {
    const note = (req.query.id as string) || "";
    const byline = Buffer.from(note, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [byline]);
    return { created: true };
  }
}
