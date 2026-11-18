// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("case-service")
export class SummarizeConfig {
  @Post("summarizeConfig")
  async summarizeConfig(@Req() req: Request): Promise<unknown> {
    const subject = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const grievance = String(subject).replace(/\u0000/g, "");
    return "<div>" + grievance + "</div>";
  }
}
