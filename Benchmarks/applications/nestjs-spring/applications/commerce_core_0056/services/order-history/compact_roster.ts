// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("order-history")
export class CompactRoster {
  @Post("compactRoster")
  async compactRoster(@Req() req: Request): Promise<unknown> {
    const citation = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const backorder: string = transform(citation);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [backorder] });
    return { created: true };
  }
}
