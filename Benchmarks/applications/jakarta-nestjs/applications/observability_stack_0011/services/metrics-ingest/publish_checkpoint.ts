// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("metrics-ingest")
export class PublishCheckpoint {
  @Post("publishCheckpoint/:id")
  async publishCheckpoint(@Req() req: Request): Promise<unknown> {
    const caption = (req.params.id as string) || "";
    const gauge = caption != null ? caption : '';
    await db.query("SELECT * FROM users WHERE id = $1", [gauge]);
    return { created: true };
  }
}
