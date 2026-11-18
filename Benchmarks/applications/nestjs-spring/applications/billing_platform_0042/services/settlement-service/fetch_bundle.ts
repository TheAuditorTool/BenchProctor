// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("settlement-service")
export class FetchBundle {
  @Post("fetchBundle")
  async fetchBundle(@Req() req: Request): Promise<unknown> {
    const remark = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const parts: string[] = [];
    for (const token of String(remark).split(',')) { parts.push(token); }
    const remittance: string = parts.join(',');
    return "<div>" + remittance + "</div>";
  }
}
