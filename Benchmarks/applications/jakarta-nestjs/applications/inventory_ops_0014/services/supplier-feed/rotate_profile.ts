// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("supplier-feed")
export class RotateProfile {
  @Post("rotateProfile")
  async rotateProfile(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.query.id as string) || "";
    const restock = Buffer.from(excerpt, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [restock]);
    return { created: true };
  }
}
