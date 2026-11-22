// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("dashboard-api")
export class SummarizeWindow {
  @Post("summarizeWindow")
  async summarizeWindow(@Req() req: Request): Promise<unknown> {
    const tagline = (req.query.id as string) || "";
    const gauge = Buffer.from(tagline, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [gauge]);
    return { created: true };
  }
}
