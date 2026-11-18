// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("alert-router")
export class CompactReceipt {
  @Post("compactReceipt/:id")
  async compactReceipt(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.params.id as string) || "";
    const gauge = excerpt != null ? excerpt : '';
    await db.query("SELECT * FROM users WHERE id = $1", [gauge]);
    return { created: true };
  }
}
