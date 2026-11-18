// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("dashboard-api")
export class FormatBundle {
  @Post("formatBundle/:id")
  async formatBundle(@Req() req: Request): Promise<unknown> {
    const headline = (req.params.id as string) || "";
    const cohort = headline != null ? headline : '';
    await db.query("SELECT * FROM users WHERE id = $1", [cohort]);
    return { created: true };
  }
}
