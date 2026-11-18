// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("bounce-handler")
export class SummarizeSchedule {
  @Post("summarizeSchedule/:id")
  async summarizeSchedule(@Req() req: Request): Promise<unknown> {
    const summary = (req.params.id as string) || "";
    const bulletin = summary != null ? summary : '';
    await db.query("SELECT * FROM users WHERE id = $1", [bulletin]);
    return { created: true };
  }
}
