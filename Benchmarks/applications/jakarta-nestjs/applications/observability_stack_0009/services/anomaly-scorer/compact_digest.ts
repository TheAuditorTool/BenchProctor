// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("anomaly-scorer")
export class CompactDigest {
  @Post("compactDigest/:id")
  async compactDigest(@Req() req: Request): Promise<unknown> {
    const summary = (req.params.id as string) || "";
    const gauge = summary != null ? summary : '';
    await db.query("SELECT * FROM users WHERE id = $1", [gauge]);
    return { created: true };
  }
}
