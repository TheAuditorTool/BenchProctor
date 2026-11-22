// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("sampling-config")
export class CollectCheckpoint {
  @Post("collectCheckpoint")
  async collectCheckpoint(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.query.id as string) || "";
    const gauge = Buffer.from(paragraph, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [gauge]);
    return { created: true };
  }
}
