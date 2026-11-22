// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("watchlist-sync")
export class FetchBundle {
  @Post("fetchBundle")
  async fetchBundle(@Req() req: Request): Promise<unknown> {
    const excerpt = process.env.RISK_INPUT_0025 || "";
    const transform = (v: string): string => v.trim();
    const verdict: string = transform(excerpt);
    if (!/^(asc|desc|name|created)$/.test(String(verdict))) { throw new BadRequestException({error:"invalid"}); }
    const grievance = verdict;
    await db.query("SELECT * FROM users ORDER BY " + grievance);
    return { created: true };
  }
}
